import json

def load_books(file_name="library.json"):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if not content.strip():  # Check if the file is empty
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []

def save_books(books, file_name="library.json"):
    with open(file_name, "w") as file:
        json.dump(books, file, indent=4)

def add_book(title, author, genre, year, status):
    books = load_books()
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "status": status
    }
    books.append(book)
    save_books(books)

def delete_book(book_id):
    books = load_books()
    updated_books = [book for book in books if book["id"] != book_id]
    
    # Reassign IDs to maintain order
    for idx, book in enumerate(updated_books):
        book["id"] = idx + 1

    save_books(updated_books)
    print(f"Cartea cu ID {book_id} a fost ștearsă.")

def search_books(keyword):
    books = load_books()
    results = [book for book in books if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]
    return results

def update_book(book_id, title=None, author=None, genre=None, year=None, status=None):
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if genre:
                book["genre"] = genre
            if year:
                book["year"] = year
            if status:
                book["status"] = status
            save_books(books)
            return
    print(f"Cartea cu ID {book_id} nu a fost găsită.")

def display_books():
    books = load_books()
    for book in books:
        print(f"ID: {book['id']}, Titlu: {book['title']}, Autor: {book['author']}, Gen: {book['genre']}, An: {book['year']}, Status: {book['status']}")
        
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
