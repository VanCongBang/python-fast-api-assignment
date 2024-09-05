from fastapi import FastAPI
from routers import users, companies, tasks

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(companies.router, prefix="/companies", tags=["companies"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])