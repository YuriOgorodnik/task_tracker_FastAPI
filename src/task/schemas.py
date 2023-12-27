from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str  # Поле для названия задачи
    created_at: datetime  # Поле для даты и времени создания задачи
    deadline: datetime  # Поле для дедлайна задачи
    is_active: bool  # Поле для статуса активности задачи
    parent_task_id: Optional[
        int
    ] = None  # Необязательное поле для идентификатора родительской задачи
    employee_id: Optional[int]  # Необязательное поле для идентификатора сотрудника


class TaskRead(BaseModel):
    id: int  # Поле для уникального идентификатора задачи
    title: str  # Поле для названия задачи
    created_at: datetime  # Поле для даты и времени создания задачи
    deadline: datetime  # Поле для дедлайна задачи
    is_active: bool  # Поле для статуса активности задачи
    parent_task_id: Optional[
        int
    ] = None  # Необязательное поле для идентификатора родительской задачи
    employee_id: Optional[int]  # Необязательное поле для идентификатора сотрудника
