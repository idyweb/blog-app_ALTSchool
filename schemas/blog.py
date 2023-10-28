from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateBlog(BaseModel):
    title: str
    content: Optional[str] = None


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    pass
