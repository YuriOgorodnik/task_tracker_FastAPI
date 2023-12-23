import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.employee.router import router as router_employee
from src.task.router import router as router_task

app = FastAPI(
    title='Task Tracker'
)

app.include_router(router_employee)
app.include_router(router_task)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
