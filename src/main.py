import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.employee.router import router as router_employee
from src.task.router import router as router_task

app = FastAPI(  # Создание экземпляра FastAPI под названием "Task Tracker"
    title="Task Tracker"  # Установка заголовка приложения
)

app.include_router(router_employee)  # Включение маршрутов сотрудников в приложение
app.include_router(router_task)  # Включение маршрутов задач в приложение

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(  # Добавление промежуточного ПО (middleware) для поддержки CORS
    CORSMiddleware,  # Использование CORS Middleware для обработки CORS
    allow_origins=origins,  # Установка разрешенных источников запросов
    allow_credentials=True,  # Разрешение отправки и получения Cookie в запросах
    allow_methods=[
        "GET",
        "POST",
        "OPTIONS",
        "DELETE",
        "PATCH",
        "PUT",
    ],  # Установка разрешенных HTTP методов
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],  # Установка разрешенных заголовков запросов
)

if __name__ == "__main__":  # Проверка, что скрипт запущен как основной
    uvicorn.run(
        "src.main:app", reload=True
    )  # Запуск FastAPI приложения с помощью uvicorn с включенной автоматической перезагрузкой
