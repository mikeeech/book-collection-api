from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, database
from datetime import date

router = APIRouter(
    prefix="/books",
    tags=["books"],
)

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        status=book.status,
        rating=book.rating,
        notes=book.notes,
        date_completed=book.date_completed
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=List[schemas.Book])
def read_books(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    genre: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Book)
    
    if status:
        query = query.filter(models.Book.status == status)
    if genre:
        query = query.filter(models.Book.genre == genre)
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (models.Book.title.ilike(search_term)) | 
            (models.Book.author.ilike(search_term))
        )
    
    return query.offset(skip).limit(limit).all()

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(database.get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(database.get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    
    if update_data.get("status") == "completed" and not db_book.date_completed:
        db_book.date_completed = date.today()
    
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(database.get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}

@router.get("/stats/reading", response_model=dict)
def reading_stats(db: Session = Depends(database.get_db)):
    total_books = db.query(models.Book).count()
    completed_books = db.query(models.Book).filter(models.Book.status == "completed").count()
    to_read_books = db.query(models.Book).filter(models.Book.status == "to_read").count()
    reading_books = db.query(models.Book).filter(models.Book.status == "reading").count()
    
    return {
        "total_books": total_books,
        "completed_books": completed_books,
        "to_read_books": to_read_books,
        "reading_books": reading_books,
        "completion_rate": round(completed_books / total_books * 100, 2) if total_books > 0 else 0
    }