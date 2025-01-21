from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Funcție pentru încărcarea cărților din fișierul JSON
def load_books():
    try:
        with open("library.json", "r") as file:
            content = file.read()
            if not content.strip():  # Verifică dacă fișierul este gol
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []

# Funcție pentru salvarea cărților în fișierul JSON
def save_books(books):
    with open("library.json", "w") as file:
        json.dump(books, file, indent=4)

# Endpoint pentru obținerea cărților
@app.route('/books', methods=['GET'])
def get_books():
    books = load_books()
    return jsonify(books)

# Endpoint pentru adăugarea unei cărți
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books = load_books()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201

# Endpoint pentru căutarea cărților
@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    books = load_books()
    filtered_books = [
        book for book in books if query in book['title'].lower() or query in book['author'].lower()
    ]
    return jsonify(filtered_books)

# Endpoint pentru ștergerea unei cărți
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books = load_books()
    books = [book for book in books if book['id'] != book_id]
    save_books(books)
    return jsonify({"message": f"Cartea cu ID {book_id} a fost ștearsă cu succes!"}), 200

# Pagina principală
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
