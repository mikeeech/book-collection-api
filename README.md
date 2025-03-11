# book-collection-api

book-collection-api is a simple REST API project built using FastAPI to manage reading lists. It allows you to track, organise and write reviews/notes about books that you've read, as well as gain insights into your reading list.

It includes the following features:

- **Managing book collection**: Add, update, view, and delete books in your collection
- **Track reading status**: Mark books as to-read, reading, completed, or finished
- **Add book ratings**: Rate books on a scale (0-5)
- **Add reading notes**: Add your thoughts and reflections for each book
- **Filter reading lists**: Search books by title, author, genre, or reading status
- **Get reading statistics**: Get insights into your reading progress and habits

And is built using:

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

# To run the project:

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mikeeech/book-collection-api.git
   cd book-collection-api
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at http://localhost:8000.

## API Documentation

Interactive API documentation is automatically generated and available at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

| Method | URL                  | Description                            |
| ------ | -------------------- | -------------------------------------- |
| GET    | /books               | List all books with optional filtering |
| POST   | /books               | Add a new book to your collection      |
| GET    | /books/{id}          | Get details of a specific book         |
| PUT    | /books/{id}          | Update book information                |
| DELETE | /books/{id}          | Remove a book from your collection     |
| GET    | /books/stats/reading | Get reading statistics                 |

## Example Use

### Adding a new book

```bash
curl -X 'POST' \
  'http://localhost:8000/books/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "The Seven Husbands of Evelyn Hugo",
  "author": "Taylor Jenkins Reid",
  "genre": "Romance",
  "status": "completed",
  "rating": 4.7,
  "notes": "I loved this book!"
}'
```

### Retrieving books with a filter

```bash
# Get all biography books
curl -X 'GET' 'http://localhost:8000/books/?genre=Biography'

# Get all books you're currently reading
curl -X 'GET' 'http://localhost:8000/books/?status=reading'

# Search for books by title or author
curl -X 'GET' 'http://localhost:8000/books/?search=Rowling'
```

## Development

### Project Structure

```
/book_collection_api/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI application setup
│   ├── models.py       # SQLAlchemy ORM models
│   ├── database.py     # Database connection setup
│   ├── schemas.py      # Pydantic models for validation
│   └── routers/
│       ├── __init__.py
│       └── books.py    # Book-related endpoints
├── requirements.txt
└── README.md
```

## License

MIT
