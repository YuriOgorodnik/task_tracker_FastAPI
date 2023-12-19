# from sqlalchemy import select, desc
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import selectinload
# from sqlalchemy.engine import Result
# from sqlalchemy.sql.functions import func
#
# from src.employee.models import employee
# from src.task.models import task
#
#
# async def get_engaged_employees(session: AsyncSession) -> list[employee]:
#     """Получает список занятых сотрудников, отсортированные по количеству активных задач"""
#     stmt = (select(
#         employee,
#         func.count(task.c.id).label('active_tasks_count')
#         ).join(employee.tasks)
#         .filter(task.c.is_active)
#         .group_by(employee.id)
#         .order_by(desc('active_tasks_count'))
#         .options(selectinload(employee.tasks))
#     )
#
#     result: Result = await session.execute(stmt)
#     employees = result.scalars().all()
#     return list(employees)
