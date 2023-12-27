from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
)  # Импорт нужных классов и типов данных из модуля sqlalchemy

from src.database import metadata

employee = Table(  # Определение таблицы "employee" с использованием класса Table
    "employee",  # Имя таблицы
    metadata,  # Объект метаданных, указывающий на базу данных, к которой привязана таблица
    Column("id", Integer, primary_key=True, doc="Уникальный идентификатор сотрудника"),
    # Столбец для уникального идентификатора сотрудника
    Column(
        "last_name", String, nullable=False, doc="Фамилия сотрудника"
    ),  # Столбец для фамилии сотрудника
    Column(
        "first_name", String, nullable=False, doc="Имя сотрудника"
    ),  # Столбец для имени сотрудника
    Column(
        "patronymic",
        String,
        nullable=True,
        doc="Отчество сотрудника (если таковое имеется)",
    ),
    # Столбец для отчества сотрудника
    Column(
        "position", String, nullable=False, doc="Должность сотрудника"
    ),  # Столбец для должности сотрудника
    Column(
        "phone_number",
        String,
        nullable=False,
        unique=True,
        doc="Номер телефона сотрудника",
    ),
    # Столбец для номера телефона сотрудника
    Column(
        "email",
        String(length=50),
        unique=True,
        nullable=False,
        doc="Электронная почта сотрудника",
    ),
    # Столбец для электронной почты сотрудника
    Column(
        "address", String(length=70), nullable=False, doc="Адрес проживания сотрудника"
    ),
    # Столбец для адреса проживания сотрудника
    Column(
        "city", String(length=30), nullable=False, doc="Город проживания сотрудника"
    ),
    # Столбец для города проживания сотрудника
    Column(
        "country", String(length=30), nullable=False, doc="Страна проживания сотрудника"
    ),
    # Столбец для страны проживания сотрудника
)
