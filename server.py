from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

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

@app.route('/books', methods=['GET'])
def get_books():
    books = load_books()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if not new_book or not all(key in new_book for key in ("title", "author", "genre", "year", "status")):
        return jsonify({"error": "Invalid data"}), 400

    books = load_books()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    books = load_books()
    filtered_books = [
        book for book in books if query in book['title'].lower() or query in book['author'].lower()
    ]
    return jsonify(filtered_books)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books = load_books()
    updated_books = [book for book in books if book['id'] != book_id]
    save_books(updated_books)
    return jsonify({"message": f"Cartea cu ID {book_id} a fost ștearsă cu succes!"}), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
