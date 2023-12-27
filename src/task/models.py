from datetime import datetime

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    TIMESTAMP,
    Boolean,
    ForeignKey,
)

from src.database import metadata
from src.employee.models import employee

task = Table(  # Определение таблицы "task" с использованием класса Table
    "task",  # Имя таблицы
    metadata,  # Объект метаданных, указывающий на базу данных, к которой привязана таблица
    Column(
        "id", Integer, primary_key=True, doc="Уникальный идентификатор задачи"
    ),  # Столбец для уникального идентификатора задачи
    Column(
        "title", String(length=300), nullable=False, doc="Наименование задачи"
    ),  # Столбец для названия задачи
    Column(
        "created_at",
        TIMESTAMP(timezone=True),
        default=datetime.utcnow,
        doc="Дата и время создания задачи",
    ),
    # Столбец для даты и времени создания задачи с указанием значения по умолчанию
    Column(
        "deadline",
        TIMESTAMP(timezone=True),
        nullable=False,
        doc="Конечная дата и время исполнения задачи",
    ),
    # Столбец для дедлайна задачи
    Column("is_active", Boolean, default=True, nullable=False, doc="Статус задачи"),
    # Столбец для статуса активности задачи
    Column(
        "parent_task_id",
        Integer,
        ForeignKey("task.id"),
        nullable=True,
        doc="Идентификатор родительской задачи",
    ),  # Столбец для идентификатора родительской задачи
    Column(
        "employee_id",
        Integer,
        ForeignKey(employee.c.id, ondelete="CASCADE"),
        nullable=True,
        doc="Идентификатор сотрудника, связанного с задачей",
    ),  # Столбец для идентификатора сотрудника, связанного с задачей
)
