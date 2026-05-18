from pydantic import BaseModel
from typing import Optional


class JobCreate(BaseModel):
    filename: str
    file_type: str


class JobResponse(BaseModel):
    id: int
    filename: str
    file_type: str
    status: str
    message: Optional[str] = None