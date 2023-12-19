from fastapi import FastAPI
from src.employee.router import router as router_employee
from src.task.router import router as router_task


app = FastAPI(
    title='Task Tracker'
)

app.include_router(router_employee)
app.include_router(router_task)
