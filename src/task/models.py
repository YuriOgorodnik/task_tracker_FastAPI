from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, Boolean, ForeignKey

from src.employee.models import employee

metadata = MetaData()

task = Table(
    "task",
    metadata,
    Column("id", Integer, primary_key=True, doc="Уникальный идентификатор задачи"),
    Column("title", String(length=300), nullable=False, doc="Наименование задачи"),
    Column("created_at", TIMESTAMP, default=datetime.utcnow, doc="Дата и время создания задачи"),
    Column("deadline", TIMESTAMP, nullable=False, doc="Конечная дата и время исполнения задачи"),
    Column("is_active", Boolean, default=True, nullable=False, doc="Статус задачи"),
    Column("parent_task_id", Integer, ForeignKey("task.id"), nullable=True,
           doc="Идентификатор родительской задачи"),
    Column("employee_id", Integer, ForeignKey(employee.c.id), nullable=True,
           doc="Идентификатор сотрудника, связанного с задачей"),
)
