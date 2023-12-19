# import asyncio
# import os
# import sys
#
# import click
# from src.commands.data import employee_data, task_data
# from src.database import get_async_session
# from src.employee.dao import EmployeesDAO
#
# from src.task.dao import TasksDAO
#
# current_file = os.path.abspath(__file__)
#
# BASE_DIR = os.path.dirname(os.path.dirname(current_file))
#
# sys.path.insert(0, BASE_DIR)
#
# src_dir = os.path.join(os.path.dirname(__file__), "..", "..")
# sys.path.append(src_dir)
#
#
# async def main():
#     try:
#         async for session in get_async_session():
#             await EmployeesDAO.clear_employee_table(session)
#             await session.commit()
#             await TasksDAO.clear_task_table(session)
#             await session.commit()
#
#             for employee, task in zip(employee_data, task_data):
#                 await EmployeesDAO.add_all_employees(session, employee)
#                 await TasksDAO.add_all_tasks(session, task)
#             await session.commit()
#             click.echo("Таблицы успешно заполнены.")
#
#     except Exception as e:
#         click.echo(f"Произошла ошибка: {e}")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
