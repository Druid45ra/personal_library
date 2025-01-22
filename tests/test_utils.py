import unittest
from utils import add_book, load_books, delete_book, search_books

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.test_book = {
            "title": "Test Title",
            "author": "Test Author",
            "genre": "Test Genre",
            "year": 2025,
            "status": "Unread"
        }
        add_book(**self.test_book)

    def test_load_books(self):
        self.assertGreater(len(load_books()), 0)

    def test_add_book(self):
        books_before = load_books()
        add_book("New Title", "New Author", "New Genre", 2023, "Unread")
        self.assertEqual(len(load_books()), len(books_before) + 1)

    def test_delete_book(self):
        books_before = load_books()
        if books_before:
            delete_book(books_before[0]["id"])
            self.assertEqual(len(load_books()), len(books_before) - 1)

    def test_search_books(self):
        self.assertGreater(len(search_books("Test Title")), 0)

    def tearDown(self):
        if load_books():
            for book in load_books():
                delete_book(book["id"])

if __name__ == '__main__':
    unittest.main()
