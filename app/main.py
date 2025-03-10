from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import books
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Collection API",
    description="A RESTful API for managing a personal book collection",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Book Collection API",
        "docs": "/docs",
        "endpoints": {
            "books": "/books",
            "reading_stats": "/books/stats/reading"
        }
    }