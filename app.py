from utils import load_books, save_books, add_book, delete_book, search_books

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

def main():
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
            book_id = int(input("ID-ul cărții de șters: "))
            delete_book(book_id)
        
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
    main()
