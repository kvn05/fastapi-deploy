from fastapi import FastAPI

app = FastAPI()

# In-memory storage for books and users (as an example)
books_db = {
    1: {"title": "1984", "author": "George Orwell"},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
}

users_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
}

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the simple FastAPI app!"}

# Route to fetch all books
@app.get("/books/")
def get_books():
    return books_db

# Route to fetch a specific book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = books_db.get(book_id)
    if book is None:
        return {"message": "Book not found"}
    return book

# Route to fetch all users
@app.get("/users/")
def get_users():
    return users_db

# Route to fetch a specific user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user is None:
        return {"message": "User not found"}
    return user
