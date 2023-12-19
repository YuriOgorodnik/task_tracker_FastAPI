from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.task.models import task

from src.task.schemas import TaskRead, TaskCreate

# from src.task.dependencies import get_least_busy_employee

router = APIRouter(
    prefix='/task',
    tags=['Tasks']
)


@router.get('/list', response_model=list[TaskRead])
async def list_tasks(session: AsyncSession = Depends(get_async_session)):
    """Получение общего списка задач"""
    query = select(task)
    result = await session.execute(query)
    return result.all()


@router.post('/create', response_model=TaskRead)
async def create_task(new_task: TaskCreate, session: AsyncSession = Depends(get_async_session)):
    """Создание задачи"""
    stmt = insert(task).values(**new_task.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get('/get/{task_id}', response_model=TaskRead)
async def get_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    """Получение информации о задаче по её идентификатору"""
    query = select(task).where(task.c.id == task_id)
    result = await session.execute(query)
    return result.one()


@router.put('/update/{task_id}', response_model=TaskRead)
async def update_task(task_id: int, updated_task: TaskRead,
                      session: AsyncSession = Depends(get_async_session)):
    """Обновление информации о задаче"""
    stmt = update(task).where(task.c.id == task_id).values(**updated_task.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete('/delete/{task_id}', response_model=dict)
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    """Удаление задачи"""
    stmt = delete(task).where(task.c.id == task_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


#
# @router.get('/important')
# async def get_important_tasks(least_busy_employee: Employee = Depends(get_least_busy_employee),
#                               session: AsyncSession = Depends(get_async_session)):
#     """
#     Список важных задач и возможных сотрудников для их выполнения.
#     Важные задачи - задачи, не взятые в работу, и от которых зависят
#     другие задачи, взятые в работу.
#     """
#     task = await services.get_important_tasks(session)
#     res_tasks = []
#     for task in task:
#         parent_task_employee_task_count = len([t for t in task.parent_task.employee.task if t.is_active])
#         least_busy_employee_task_count = len([t for t in least_busy_employee.task if t.is_active])
#         res = parent_task_employee_task_count - least_busy_employee_task_count
#         if res <= 2:
#             available_employee = task.parent_task.employee
#         else:
#             available_employee = least_busy_employee
#
#         task_data = {
#             'task': TaskRead.model_validate(task, from_attributes=True),
#             'available_employee': available_employee.__str__()
#         }
#         res_tasks.append(task_data)
#
#     return res_tasks
#
#
# @router.get('/important', response_model=List[TaskAssignee])
# async def get_tasks_and_assignees(session: AsyncSession = Depends(get_async_session)):
#     """Получение списка задач и возможных исполнителей"""
#     return await services.find_tasks_and_assignees(session)
#
#
# @router.get('/least-busy-employee', response_model=EmployeeRead)
# async def get_least_busy_employee(session: AsyncSession = Depends(get_async_session)):
#     """Получение наименее загруженного сотрудника"""
#     return await services.get_least_busy_employee(session)

