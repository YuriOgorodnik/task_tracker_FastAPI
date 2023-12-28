from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
)

from src.database import metadata

employee = Table(  # Определение таблицы "employee" с использованием класса Table
    "employee",  # Имя таблицы
    metadata,  # Объект метаданных, указывающий на базу данных, к которой привязана таблица
    Column("id", Integer, primary_key=True, doc="Уникальный идентификатор сотрудника"),
    Column(
        "last_name", String, nullable=False, doc="Фамилия сотрудника"
    ),
    Column(
        "first_name", String, nullable=False, doc="Имя сотрудника"
    ),
    Column(
        "patronymic",
        String,
        nullable=True,
        doc="Отчество сотрудника (если таковое имеется)",
    ),
    Column(
        "position", String, nullable=False, doc="Должность сотрудника"
    ),
    Column(
        "phone_number",
        String,
        nullable=False,
        unique=True,
        doc="Номер телефона сотрудника",
    ),
    Column(
        "email",
        String(length=50),
        unique=True,
        nullable=False,
        doc="Электронная почта сотрудника",
    ),
    Column(
        "address", String(length=70), nullable=False, doc="Адрес проживания сотрудника"
    ),
    Column(
        "city", String(length=30), nullable=False, doc="Город проживания сотрудника"
    ),
    Column(
        "country", String(length=30), nullable=False, doc="Страна проживания сотрудника"
    ),
)
