import json

def load_books():
    try:
        with open("library.json", "r") as file:
            content = file.read()
            if not content.strip():  # Check if the file is empty
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []

def save_books(books):
    with open("library.json", "w") as file:
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
