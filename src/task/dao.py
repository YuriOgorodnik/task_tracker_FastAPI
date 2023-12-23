from sqlalchemy import delete, text, insert, select, update

from src.task.models import task


class TaskDAO:
    @classmethod
    async def add_task(cls, session, task_data):
        """Добавление новой задачи в базу данных"""
        stmt = insert(task).values(**task_data)
        await session.execute(stmt)

    @classmethod
    async def clear_task_table(cls, session):
        """Очищение таблицы задач в базе данных"""
        try:
            stmt = delete(task)
            await session.execute(stmt)
            await session.execute(text("ALTER SEQUENCE task_id_seq RESTART WITH 1"))
            print(f"Таблица Task очищена!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    @classmethod
    async def get_all_tasks(cls, session):
        """Получение списка всех задач, имеющихся в базе данных"""
        stmt = select(task)
        result = await session.execute(stmt)
        return result.fetchall()

    @classmethod
    async def get_task_by_id(cls, session, task_id):
        """Получение информации о задаче по её идентификатору"""
        stmt = select(task).where(task.c.id == task_id)
        result = await session.execute(stmt)
        return result.fetchone()

    @classmethod
    async def update_task(cls, session, task_id, updated_task_data):
        """Обновление информации о задаче по её идентификатору"""
        stmt = update(task).where(task.c.id == task_id).values(**updated_task_data)
        await session.execute(stmt)

    @classmethod
    async def delete_task(cls, session, task_id):
        """Удаление задачи по её идентификатору"""
        stmt = delete(task).where(task.c.id == task_id)
        await session.execute(stmt)

    @classmethod
    async def get_dependent_unassigned_tasks(cls, session):
        """Получение списка не назначенных задач, от которых зависят другие задачи"""
        stmt = select(task).where(task.c.employee_id.is_(None))
        result = await session.execute(stmt)
        return result.fetchall()
