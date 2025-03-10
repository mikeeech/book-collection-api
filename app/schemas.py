from pydantic import BaseModel, Field
from datetime import date
from enum import Enum
from typing import Optional

class ReadingStatus(str, Enum):
    to_read = "to_read"
    reading = "reading"
    finished = "finished"
    abandoned = "abandoned"

class BookBase(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    status: ReadingStatus = ReadingStatus.to_read
    rating: Optional[float] = None
    notes: Optional[str] = None
    date_completed: Optional[date] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    status: Optional[ReadingStatus] = None
    rating: Optional[float] = Field(None, ge=0, le=5)
    notes: Optional[str] = None
    date_completed: Optional[date] = None

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
