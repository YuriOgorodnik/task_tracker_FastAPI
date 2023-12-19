from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.employee.models import employee
from src.employee.schemas import EmployeeCreate, EmployeeRead
from src.task.models import task

router = APIRouter(
    prefix='/employee',
    tags=['Employees']
)


@router.get('/list', response_model=list[EmployeeRead])
async def list_employees(session: AsyncSession = Depends(get_async_session)):
    """Получение общего списка сотрудников"""
    query = select(employee)
    result = await session.execute(query)
    return result.all()


@router.post('/create', response_model=EmployeeRead)
async def create_employee(new_employee: EmployeeCreate, session: AsyncSession = Depends(get_async_session)):
    """Создание сотрудника"""
    stmt = insert(employee).values(**new_employee.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get('/get/{employee_id}', response_model=EmployeeRead)
async def get_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    """Получение информации о сотруднике по его идентификатору"""
    query = select(employee).where(employee.c.id == employee_id)
    result = await session.execute(query)
    return result.one()


@router.put('/update/{employee_id}', response_model=EmployeeRead)
async def update_employee(employee_id: int, updated_employee: EmployeeRead,
                          session: AsyncSession = Depends(get_async_session)):
    """Обновление информации о сотруднике"""
    stmt = update(employee).where(employee.c.id == employee_id).values(**updated_employee.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete('/delete/{employee_id}', response_model=dict)
async def delete_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    """Удаление сотрудника"""
    stmt = delete(employee).where(employee.c.id == employee_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


# @router.get('/employees_with_tasks', response_model=list[EmployeeRead])
# async def get_employees_with_tasks(session: AsyncSession = Depends(get_async_session)):
#     """Получение списка сотрудников и их задач, отсортированных по количеству активных задач"""
#
#     # Получаем список сотрудников
#     query = select(employee)
#     employees = await session.execute(query)
#     employees = employees.all()
#
#
#     # Получаем количество активных задач для каждого сотрудника и сортируем их
#     employees_with_tasks = []
#     for emp in employees:
#         active_tasks_count = (
#             await session.execute(
#                 select(func.count(task.c.id))
#                 .where(task.c.employee_id == emp.id)
#                 .where(task.c.status == "active")
#             )
#         ).scalar()
#         employees_with_tasks.append({"employee": emp, "active_tasks_count": active_tasks_count})
#
#     employees_with_tasks.sort(key=lambda x: x["active_tasks_count"], reverse=True)
#
#     return [emp["employee"] for emp in employees_with_tasks]
