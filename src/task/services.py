# from typing import List, Optional
#
# from sqlalchemy import select, and_
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import joinedload
# from sqlalchemy.engine import Result
#
# from src.employee.models import Employee
# from src.task.models import Task
# from src.task.schemas import TaskCreate, TaskUpdate, TaskRead
#
#
# async def list_tasks(session: AsyncSession) -> List[TaskRead]:
#     """Получает список всех задач"""
#     task = await session.execute(select(Task))
#     return task.scalars().all()
#
#
# async def create_task(new_task: TaskCreate, session: AsyncSession) -> TaskRead:
#     """Создает новоую задачу"""
#     task = Task(**new_task.model_dump())
#     session.add(task)
#     await session.commit()
#     return task
#
#
# async def get_task(task_id: int, session: AsyncSession) -> Optional[TaskRead]:
#     """Получает данные одной задачи по ее id"""
#     task = await session.get(Task, task_id)
#     return task
#
#
# async def update_task(task_id: int, updated_task: TaskUpdate, session: AsyncSession) -> Optional[TaskRead]:
#     """Обновляет данные по задаче"""
#     task = await session.get(Task, task_id)
#     if task:
#         for field, value in updated_task:
#             setattr(task, field, value)
#         await session.commit()
#         return task
#     return None
#
#
# async def delete_task(task_id: int, session: AsyncSession) -> bool:
#     """Удаляет задачу"""
#     task = await session.get(Task, task_id)
#     if task:
#         session.delete(task)
#         await session.commit()
#         return True
#     return False
#
#
# async def get_important_tasks(session: AsyncSession):
#     """Получает список важных задач"""
#     stmt = select(Task).outerjoin(
#         Employee, Task.employee_id == Employee.id
#     ).filter(
#         Task.employee_id.is_(None),
#         Task.parent_task.has(Task.employee_id.isnot(None))
#     ).options(joinedload(Task.parent_task).joinedload(Task.employee).joinedload(Employee.task))
#
#     result: Result = await session.execute(stmt)
#     task = result.unique().scalars().all()
#
#     return task
#
#
# async def find_tasks_and_assignees(session: AsyncSession) -> List[dict]:
#     subquery = (
#         select(Task.id)
#         .where(and_(Task.is_active == False, Task.parent_task_id.isnot(None)))
#         .correlate(Task)
#     )
#     task = await session.execute(
#         select(Task, Employee)
#         .join(Employee, isouter=True)
#         .filter(and_(Task.id.in_(subquery), Employee.active_task_count < 3))
#     )
#
#     result = []
#     for task, employee in task:
#         task_info = {
#             "title": task.title,
#             "deadline": task.deadline,
#             "assignee": f"{employee.last_name} {employee.first_name} {employee.patronymic}"
#         }
#         result.append(task_info)
#
#     return result
#
#
# async def get_least_busy_employee(session: AsyncSession) -> Optional[Employee]:
#     employee = await session.execute(
#         select(Employee)
#         .order_by(Employee.active_task_count)
#         .limit(1)
#     ).scalar()
#     return employee
