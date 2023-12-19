from pydantic import BaseModel
from typing import Optional


class EmployeeCreate(BaseModel):
    last_name: str
    first_name: str
    patronymic: Optional[str] = None
    position: str
    phone_number: str
    email: str
    address: str
    city: str
    country: str


class EmployeeRead(BaseModel):
    id: int
    last_name: str
    first_name: str
    patronymic: Optional[str] = None
    position: str
    phone_number: str
    email: str
    address: str
    city: str
    country: str
