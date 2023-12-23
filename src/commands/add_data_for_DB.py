import asyncio
from datetime import datetime

from src.commands.data import employee_data, task_data
from src.employee.dao import EmployeeDAO
from src.task.dao import TaskDAO
from src.database import get_async_session


async def populate_database():
    async for session in get_async_session():
        await TaskDAO.clear_task_table(session)
        await EmployeeDAO.clear_employee_table(session)

        for employee in employee_data:
            await EmployeeDAO.add_employee(session, employee)

        for task in task_data:
            task["created_at"] = datetime.fromisoformat(task["created_at"])
            task["deadline"] = datetime.fromisoformat(task["deadline"])
            await TaskDAO.add_task(session, task)

        await session.commit()


if __name__ == "__main__":
    asyncio.run(populate_database())
