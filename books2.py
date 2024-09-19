from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

app = FastAPI()

BOOKS = [
    {'title': 'Title one', 'author': 'Author one', 'category':'science'},
    {'title': 'Title tow', 'author': 'Author tow', 'category':'science'},
    {'title': 'Title three', 'author': 'Author three', 'category':'hostory'},
    {'title': 'Title four', 'author': 'Author four', 'category':'math'},
    {'title': 'Title five', 'author': 'Author five', 'category':'math'},
    {'title': 'Title six', 'author': 'Author tow', 'category':'math'}
]

@app.get("/books/all")
async def read_all_books():
    return BOOKS


# Path Parameters
@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}


# Query Parameters
@app.get("/books/")
def read_category_by_query(category: str):
    books_to_return = [] #empty list
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#  post method -- adding extra data
@app.post("/books/create_book")
# important not: Get cannot have a body
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# Post method -- Updating data
@app.put("/books/update_book")
async def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book

# Delete method
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i) # pop func remove element from the list BOOKS
            break


# Create a new API Endpoint
# that can fetch all books from a specific author using
# either Path Parameters or Query Parameters.

#using query parameters
@app.get("/books/book_by_author/")
async def get_all_author_books_by_query(author_name: str):
    books_by_author = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            books_by_author.append(book)
    return books_by_author

#using path parameters
@app.get("/books/book_by_author/{author_name}")
async  def get_all_author_books(author_name: str):
    books_by_author = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author_name.casefold():
            books_by_author.append(BOOKS[i])

    return books_by_author