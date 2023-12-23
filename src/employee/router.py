from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.employee.dao import EmployeeDAO
from src.employee.schemas import EmployeeRead

router = APIRouter(
    prefix='/employee',
    tags=['Employees']
)


@router.get('/list', response_model=List[EmployeeRead])
async def list_employees(session: AsyncSession = Depends(get_async_session)):
    """Получение общего списка сотрудников"""
    employees = await EmployeeDAO.get_all_employees(session)
    return employees


@router.post('/create')
async def create_employee(employee_data: dict, session: AsyncSession = Depends(get_async_session)):
    """Создание нового сотрудника"""
    await EmployeeDAO.add_employee(session, employee_data)
    await session.commit()
    return {"message": "Employee created successfully"}


@router.get('/get/{employee_id}')
async def get_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    """Получение информации о сотруднике по его идентификатору"""
    db_employee = await EmployeeDAO.get_employee_by_id(session, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@router.put('/update/{employee_id}', response_model=EmployeeRead)
async def update_employee(employee_id: int, employee_data: dict, session: AsyncSession = Depends(get_async_session)):
    """Обновление информации о сотруднике"""
    existing_employee = await EmployeeDAO.get_employee_by_id(session, employee_id)
    if existing_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    await EmployeeDAO.update_employee(session, employee_id, employee_data)
    await session.commit()
    return await EmployeeDAO.get_employee_by_id(session, employee_id)


@router.delete('/delete/{employee_id}', response_model=dict)
async def delete_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    """Удаление сотрудника"""
    existing_employee = await EmployeeDAO.get_employee_by_id(session, employee_id)
    if existing_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    await EmployeeDAO.delete_employee(session, employee_id)
    await session.commit()
    return {"message": "Employee deleted successfully"}


@router.get("/busy_employees", response_model=List[dict])
async def busy_employees(session: AsyncSession = Depends(get_async_session)):
    """Получение списка сотрудников с количеством их активных задач"""
    employees_with_tasks = await EmployeeDAO.get_employees_with_active_tasks(session)
    result = [{"employee": employee[0], "last_name": employee[1], "first_name": employee[2], "patronymic": employee[3],
               "position": employee[4], "active_tasks_count": employee[-1]} for employee in employees_with_tasks]
    return result
