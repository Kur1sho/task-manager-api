from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    status: str = Field(default="todo")

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config:
        from_attributes = True  # pydantic v2 (reads from ORM objects)
