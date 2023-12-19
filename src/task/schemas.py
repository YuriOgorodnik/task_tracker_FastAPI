from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    created_at: datetime
    deadline: datetime
    is_active: bool
    parent_task_id: Optional[int] = None
    employee_id: Optional[int]


class TaskRead(BaseModel):
    id: int
    title: str
    created_at: datetime
    deadline: datetime
    is_active: bool
    parent_task_id: Optional[int] = None
    employee_id: Optional[int]
