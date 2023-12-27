from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.employee.dao import EmployeeDAO
from src.employee.services import get_eligible_employees
from src.task.dao import TaskDAO

from src.task.schemas import TaskRead, TaskCreate
from src.tasks.tasks import send_assign_task_email

router = APIRouter(prefix="/task", tags=["Tasks"])


@router.get("/list", response_model=List[TaskRead])
async def list_tasks(session: AsyncSession = Depends(get_async_session)):
    """Получение общего списка задач"""
    tasks = await TaskDAO.get_all_tasks(session)
    return tasks


@router.post("/create", response_model=TaskRead)
async def create_task(
    new_task: TaskCreate, session: AsyncSession = Depends(get_async_session)
):
    """Создание новой задачи"""
    created_task = await TaskDAO.add_task(session, new_task.dict())
    await session.commit()

    # Получаем информацию о сотруднике
    employee = await EmployeeDAO.get_employee_by_id(session, new_task.employee_id)

    # Добавляем отправку уведомления на электронную почту сотруднику в фоновые задачи
    send_assign_task_email(
        employee.first_name, employee.email, new_task.title, new_task.deadline
    )

    return created_task


@router.get("/get/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    """Получение информации о задаче по её идентификатору"""
    db_task = await TaskDAO.get_task_by_id(session, task_id)
    return db_task


@router.put("/update/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    updated_task: TaskRead,
    session: AsyncSession = Depends(get_async_session),
):
    """Обновление информации о задаче по её идентификатору"""
    await TaskDAO.update_task(session, task_id, updated_task.dict(exclude_unset=True))
    await session.commit()
    return updated_task


@router.delete("/delete/{task_id}", response_model=dict)
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    """Удаление задачи по её идентификатору"""
    await TaskDAO.delete_task(session, task_id)
    await session.commit()
    return {"status": "success"}


@router.get("/important_tasks", response_model=List[dict])
async def important_tasks(session: AsyncSession = Depends(get_async_session)):
    """Получение списка важных задач"""
    dependent_unassigned_tasks = await TaskDAO.get_dependent_unassigned_tasks(session)
    result = []

    for task_row in dependent_unassigned_tasks:
        (
            task_id,
            title,
            created_at,
            deadline,
            is_active,
            parent_task_id,
            employee_id,
        ) = task_row
        eligible_employees = await get_eligible_employees(session, task_id)
        result.append(
            {
                "important_task": {
                    "id": task_id,
                    "title": title,
                    "deadline": deadline,
                    "is_active": is_active,
                    "eligible_employees": eligible_employees,
                }
            }
        )

    return result
