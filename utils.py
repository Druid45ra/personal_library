import json

def load_books():
    with open('library.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def save_books(books):
    with open('library.json', 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=4, ensure_ascii=False)

def add_book(title, author, genre, year, status):
    books = load_books()
    new_book = {
        "id": max(book["id"] for book in books) + 1 if books else 1,
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "status": status
    }
    books.append(new_book)
    save_books(books)

def delete_book(book_id: int) -> None:
    """Delete a book from the library"""
    books = load_books()
    updated_books = [book for book in books if book["id"] != book_id]

    # Reassign IDs to maintain order
    for idx, book in enumerate(updated_books, start=1):
        book["id"] = idx

    save_books(updated_books)
    print(f"Cartea cu ID {book_id} a fost ștearsă.")

def search_books(keyword: str) -> list:
    books = load_books()
    return [book for book in books if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]

def update_book(
    book_id: int, title: str | None = None, author: str | None = None,
    genre: str | None = None, year: str | None = None, status: str | None = None
) -> None:
    books = load_books()
    found_book = next((book for book in books if book["id"] == book_id), None)
    if found_book is None:
        print(f"Cartea cu ID {book_id} nu a fost găsită.")
        return
    if title:
        found_book["title"] = title
    if author:
        found_book["author"] = author
    if genre:
        found_book["genre"] = genre
    if year:
        found_book["year"] = year
    if status:
        found_book["status"] = status
    save_books(books)

def display_books() -> None:
    """Display all books in the library"""
    books = load_books()
    for book in books:
        print(
            f"ID: {book['id']}, Titlu: {book['title']}, Autor: {book['author']}, "
            f"Gen: {book['genre']}, An: {book['year']}, Status: {book['status']}"
        )
        
if __name__ == "__main__":
    print("[TEST] Adăugare carte")
    add_book("Test Book", "Test Author", "Test Genre", "2025", "Unread")
    display_books()

    print("\n[TEST] Ștergere carte")
    delete_book(1)
    display_books()

    print("\n[TEST] Căutare carte")
    results = search_books("Test")
    print(results)
