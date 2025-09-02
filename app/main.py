from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import users, tasks 


app = FastAPI(title="Task Manager API")

# create database tables
Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])

@app.get("/")
def root():
    return {"status": "Task Manager API is running "}
