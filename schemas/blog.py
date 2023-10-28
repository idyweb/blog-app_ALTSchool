from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateBlog(BaseModel):
    title: str
    content: Optional[str] = None
    author_id: int


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    title: str
    content: str
    author_id: int
    created_at: datetime
