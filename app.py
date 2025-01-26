from utils import load_books, save_books, add_book, delete_book, search_books
from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint pentru afișarea tuturor cărților
@app.route("/books", methods=["GET"])
def get_books():
    books = load_books()
    return jsonify(books), 200

# Endpoint pentru adăugarea unei cărți
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "Titlu și autor sunt obligatorii!"}), 400

    add_book(
        title=data["title"],
        author=data["author"],
        genre=data.get("genre", ""),
        year=data.get("year", ""),
        status=data.get("status", "necitită")
    )
    return jsonify({"message": "Cartea a fost adăugată!"}), 201

# Endpoint pentru ștergerea unei cărți
@app.route("/books/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):
    books = load_books()
    if not any(book["id"] == book_id for book in books):
        return jsonify({"error": "Cartea nu există!"}), 404

    delete_book(book_id)
    return jsonify({"message": "Cartea a fost ștearsă!"}), 200

# Endpoint pentru căutarea cărților
@app.route("/search", methods=["GET"])
def search_for_books():
    keyword = request.args.get("query", "")
    results = search_books(keyword)
    return jsonify(results), 200

# Funcția pentru rularea aplicației în terminal
def run_terminal_app():
    def display_menu():
        print("\n1. Adaugă o carte")
        print("2. Afișează toate cărțile")
        print("3. Șterge o carte")
        print("4. Caută cărți")
        print("5. Ieșire")

    def get_book_info():
        title = input("Titlu: ")
        author = input("Autor: ")
        genre = input("Gen: ")
        year = input("An publicare: ")
        while not year.isdigit():
            year = input("An publicare (număr valid): ")
        status = input("Stare (citită/necitită): ")
        return title, author, genre, year, status

    def display_books(books):
        if not books:
            print("Biblioteca este goală.")
        else:
            for book in books:
                print(f"ID: {book['id']}, Titlu: {book['title']}, Autor: {book['author']}, Gen: {book['genre']}, An: {book['year']}, Stare: {book['status']}")

    def display_search_results(results):
        if not results:
            print("Nu au fost găsite cărți.")
        else:
            for book in results:
                print(f"Titlu: {book['title']}, Autor: {book['author']}")

    print("=== Biblioteca Personală ===")
    while True:
        display_menu()
        choice = input("Alege o opțiune: ")

        if choice == "1":
            title, author, genre, year, status = get_book_info()
            add_book(title, author, genre, year, status)
            print("Cartea a fost adăugată cu succes!")

        elif choice == "2":
            books = load_books()
            display_books(books)

        elif choice == "3":
            try:
                book_id = int(input("ID-ul cărții de șters: "))
                delete_book(book_id)
            except ValueError:
                print("ID-ul trebuie să fie un număr.")

        elif choice == "4":
            keyword = input("Caută (titlu sau autor): ")
            results = search_books(keyword)
            display_search_results(results)

        elif choice == "5":
            print("La revedere!")
            break

        else:
            print("Opțiune invalidă!")

if __name__ == "__main__":
    mode = input("Pornești ca server (S) sau aplicație terminal (T)? ").strip().upper()
    if mode == "S":
        print("=== Pornire ca server ===")
        app.run(debug=True)
    elif mode == "T":
        print("=== Pornire aplicație terminal ===")
        run_terminal_app()
    else:
        print("Opțiune invalidă! Alege 'S' pentru server sau 'T' pentru terminal.")
