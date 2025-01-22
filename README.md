
# Personal Library

A simple Flask-based web application to manage a personal book collection. It allows you to:

- Add new books to your collection.
- Display all books in the collection.
- Delete books from the collection.
- Search books by title or author.

## Features

- **Add books**: Add a new book with details like title, author, genre, year of publication, and status.
- **View books**: Displays a list of all books in the collection.
- **Delete books**: Allows you to delete books from the collection.
- **Search books**: You can search for books by title or author.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data storage**: JSON file (`library.json`)

## Getting Started

To get this project up and running on your local machine:

### Prerequisites

1. **Python 3.x**: Make sure Python is installed on your machine. If not, download and install it from [python.org](https://www.python.org/downloads/).
2. **Flask**: Install Flask using pip.
   ```bash
   pip install Flask

Setting Up the Project

1. Clone the repository:

git clone https://github.com/your-username/personal-library.git


2. Navigate into the project directory:

cd personal-library


3. Run the Flask application:

python server.py


4. Open the application in your browser by navigating to http://127.0.0.1:5000/.



Project Structure

server.py: Main Flask server script.

frontend/index.html: The HTML interface for the library management.

frontend/style.css: The CSS styles for the app.

frontend/script.js: JavaScript for handling front-end functionality.

library.json: The file where the books are saved.


Endpoints

GET /books

Fetches all the books in the collection.

POST /books

Adds a new book to the collection. You need to provide the book data in JSON format:

{
  "title": "Book Title",
  "author": "Author Name",
  "genre": "Genre",
  "year": "2023",
  "status": "Available"
}

DELETE /books/<book_id>

Deletes a book from the collection by its id.

GET /search?query=<query>

Searches for books by title or author.

Usage

1. Add a book: Fill out the form in the web interface with the book's details and submit it.


2. View books: View a list of all added books.


3. Delete a book: Click the "Delete" button next to the book to remove it from the collection.


4. Search books: Use the search bar to search for books by title or author.



Future Enhancements

Add user authentication (login/signup).

Allow users to edit book details.

Implement pagination for displaying books.

Improve search functionality with more advanced filtering options.


License

This project is licensed under the MIT License

   
