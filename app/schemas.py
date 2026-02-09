from pydantic import BaseModel, Field, ConfigDict

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    status: str = Field(default="todo")

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str

    model_config = ConfigDict(from_attributes=True)  # pydantic v2 (reads from ORM objects)


class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=8, max_length=128)

class UserOut(BaseModel):
    id: int
    email: str

    model_config = ConfigDict(from_attributes=True)  # pydantic v2 (reads from ORM objects)

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    

