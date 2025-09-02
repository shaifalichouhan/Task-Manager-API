from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str | None = "Pending"

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
