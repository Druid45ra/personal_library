import unittest
from utils import add_book, load_books, delete_book, search_books

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.test_book = {
            "title": "Test Title",
            "author": "Test Author",
            "genre": "Test Genre",
            "year": 2025,
            "status": "Unread"
        }
        add_book(self.test_book["title"], self.test_book["author"], self.test_book["genre"], self.test_book["year"], self.test_book["status"])

    def test_load_books(self):
        books = load_books()
        self.assertGreater(len(books), 0)

    def test_add_book(self):
        books_before = load_books()
        add_book("New Title", "New Author", "New Genre", 2023, "Unread")
        books_after = load_books()
        self.assertEqual(len(books_after), len(books_before) + 1)

    def test_delete_book(self):
        books_before = load_books()
        delete_book(1)  # Assuming the first book has ID 1
        books_after = load_books()
        self.assertEqual(len(books_after), len(books_before) - 1)

    def test_search_books(self):
        results = search_books("Test Title")
        self.assertGreater(len(results), 0)

    def tearDown(self):
        # This method will run after each test
        # Clean up the library.json file if necessary
        pass

if __name__ == '__main__':
    unittest.main()
