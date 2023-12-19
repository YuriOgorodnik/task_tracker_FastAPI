from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

employee = Table(
    "employee",
    metadata,
    Column("id", Integer, primary_key=True, doc="Уникальный идентификатор сотрудника"),
    Column("last_name", String, nullable=False, doc="Фамилия сотрудника"),
    Column("first_name", String, nullable=False, doc="Имя сотрудника"),
    Column("patronymic", String, nullable=True, doc="Отчество сотрудника (если таковое имеется)"),
    Column("position", String, nullable=False, doc="Должность сотрудника"),
    Column("phone_number", String, nullable=False, unique=True, doc="Номер телефона сотрудника"),
    Column("email", String(length=50), unique=True, nullable=False,
           doc="Электронная почта сотрудника"),
    Column("address", String(length=70), nullable=False, doc="Адрес проживания сотрудника"),
    Column("city", String(length=30), nullable=False, doc="Город проживания сотрудника"),
    Column("country", String(length=30), nullable=False, doc="Страна проживания сотрудника"),
)
