import json

FILE_PATH = "library.json"

def load_books():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(FILE_PATH, "w") as file:
        json.dump(books, file, indent=4)

def add_book(title, author, genre, year, status):
    books = load_books()
    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "status": status
    }
    books.append(new_book)
    save_books(books)
    print(f"Cartea '{title}' a fost adăugată.")
    
    import unittest
from utils import add_book, load_books, save_books

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        # Adaugă o carte fictivă
        add_book("Test Title", "Test Author", "Test Genre", 2025, "Unread")
        books = load_books()
        self.assertEqual(books[-1]['title'], "Test Title")

if __name__ == '__main__':
    unittest.main()

