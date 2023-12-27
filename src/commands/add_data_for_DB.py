import asyncio
from datetime import datetime

from src.commands.data import employee_data, task_data
from src.employee.dao import EmployeeDAO
from src.task.dao import TaskDAO
from src.database import get_async_session


async def populate_database():
    async for session in get_async_session():  # Цикл по асинхронному получению сессии из get_async_session
        await TaskDAO.clear_task_table(
            session
        )  # Очистка таблицы задач с использованием TaskDAO
        await EmployeeDAO.clear_employee_table(
            session
        )  # Очистка таблицы сотрудников с использованием EmployeeDAO

        for employee in employee_data:  # Цикл по данным о сотрудниках
            await EmployeeDAO.add_employee(
                session, employee
            )  # Добавление сотрудника с использованием EmployeeDAO

        for task in task_data:  # Цикл по данным о задачах
            task["created_at"] = datetime.fromisoformat(
                task["created_at"]
            )  # Преобразование времени создания задачи из ISO формата
            task["deadline"] = datetime.fromisoformat(
                task["deadline"]
            )  # Преобразование дедлайна задачи из ISO формата
            await TaskDAO.add_task(
                session, task
            )  # Добавление задачи с использованием TaskDAO

        await session.commit()  # Фиксация изменений в сессии


if __name__ == "__main__":  # Проверка, что скрипт запущен как основной
    asyncio.run(
        populate_database()
    )  # Запуск асинхронной операции populate_database с помощью asyncio
