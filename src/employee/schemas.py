from pydantic import BaseModel
from typing import Optional


class EmployeeRead(BaseModel):
    id: int  # Поле для уникального идентификатора сотрудника
    last_name: str  # Поле для фамилии сотрудника
    first_name: str  # Поле для имени сотрудника
    patronymic: Optional[str] = None  # Необязательное поле для отчества сотрудника
    position: str  # Поле для должности сотрудника
    phone_number: str  # Поле для номера телефона сотрудника
    email: str  # Поле для электронной почты сотрудника
    address: str  # Поле для адреса проживания сотрудника
    city: str  # Поле для города проживания сотрудника
    country: str  # Поле для страны проживания сотрудника
