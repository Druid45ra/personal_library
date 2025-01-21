import unittest
from utils import add_book, load_books

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        add_book("Test Title", "Test Author", "Test Genre", 2025, "Unread")
        books = load_books()
        self.assertEqual(books[-1]['title'], "Test Title")

if __name__ == '__main__':
    unittest.main()
