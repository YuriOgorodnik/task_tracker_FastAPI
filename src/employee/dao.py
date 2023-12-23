from sqlalchemy import delete, text, insert, select, update, func, desc

from src.employee.models import employee
from src.task.models import task


class EmployeeDAO:

    @classmethod
    async def add_employee(cls, session, employee_data):
        """Добавление нового сотрудника в базу данных"""
        stmt = insert(employee).values(**employee_data)
        await session.execute(stmt)

    @classmethod
    async def clear_employee_table(cls, session):
        """Очищение таблицы сотрудников в базе данных"""
        try:
            stmt = delete(employee)
            await session.execute(stmt)
            await session.execute(text("ALTER SEQUENCE employee_id_seq RESTART WITH 1"))
            print(f"Таблица Employee очищена!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    @classmethod
    async def get_all_employees(cls, session):
        """Получение списка всех сотрудников, имеющихся в базе данных"""
        stmt = select(employee)
        result = await session.execute(stmt)
        return result.fetchall()

    @classmethod
    async def get_employee_by_id(cls, session, employee_id):
        """Получение информации о сотруднике по его идентификатору"""
        stmt = select(employee).where(employee.c.id == employee_id)
        result = await session.execute(stmt)
        return result.fetchone()._mapping

    @classmethod
    async def update_employee(cls, session, employee_id, employee_data):
        """Обновление информации о сотруднике по его идентификатору"""
        stmt = update(employee).where(employee.c.id == employee_id).values(**employee_data)
        await session.execute(stmt)

    @classmethod
    async def delete_employee(cls, session, employee_id):
        """Удаление сотрудника по его идентификатору"""
        stmt = delete(employee).where(employee.c.id == employee_id)
        await session.execute(stmt)

    @classmethod
    async def get_employee_tasks(cls, session, employee_id):
        """Получение списка задач, связанных с сотрудником по его идентификатору"""
        stmt = select(task).where(task.c.employee_id == employee_id)
        result = await session.execute(stmt)
        return result.fetchall()

    @classmethod
    async def get_employees_with_active_tasks(cls, session):
        """Получение списка сотрудников с количеством их активных задач, отсортированных по убыванию активных задач"""
        stmt = select(employee, func.count(task.c.id).label('active_tasks_count')). \
            outerjoin(task, employee.c.id == task.c.employee_id). \
            where(task.c.is_active == True).group_by(employee.c.id). \
            order_by(desc('active_tasks_count'))
        result = await session.execute(stmt)
        return result.fetchall()
