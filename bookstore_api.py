
import requests

API_URL = "https://6aec303efc3b911e6fd4b494.mockapi.io/books"


# GET: Retrieve all books
def get_books():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        print("\nALL BOOKS:")
        print(response.json())
        print("Status:", response.status_code)
    except requests.exceptions.HTTPError as error:
        print("GET Error:", error)


# POST: Add a new book
def add_book(book):
    try:
        response = requests.post(API_URL, json=book)
        response.raise_for_status()
        print("\nBOOK ADDED:")
        print(response.json())
        print("Status:", response.status_code)
    except requests.exceptions.HTTPError as error:
        print("POST Error:", error)


# PUT: Update an existing book
def update_book(book_id, book):
    try:
        response = requests.put(
            f"{API_URL}/{book_id}", json=book
        )
        response.raise_for_status()
        print("\nBOOK UPDATED:")
        print(response.json())
        print("Status:", response.status_code)
    except requests.exceptions.HTTPError as error:
        print("PUT Error:", error)


# DELETE: Remove a book
def delete_book(book_id):
    try:
        response = requests.delete(f"{API_URL}/{book_id}")
        response.raise_for_status()
        print("\nBOOK DELETED")
        print("Status:", response.status_code)
    except requests.exceptions.HTTPError as error:
        print("DELETE Error:", error)


# Check deleted book
def check_deleted_book(book_id):
    try:
        response = requests.get(f"{API_URL}/{book_id}")
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError:
        print("\nDeletion confirmed: Book not found.")


# MAIN PROGRAM

if __name__ == "__main__":
    # 1. GET all books
    get_books()