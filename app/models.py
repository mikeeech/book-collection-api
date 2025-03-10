from sqlalchemy import Column, Integer, String, Float, Text, Enum, Date
from sqlalchemy.sql import func
from .database import Base
import enum

class ReadingStatus(enum.Enum):
    to_read = "to_read"
    reading = "reading"
    finished = "finished"
    abandoned = "abandoned"

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    genre = Column(String)
    status = Column(String, default=ReadingStatus.to_read.value)
    rating = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    date_added = Column(Date, default=func.current_date())
    date_completed = Column(Date, nullable=True)