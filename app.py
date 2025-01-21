from utils import load_books, save_books, add_book, list_books, delete_book, search_books

def main():
    while True:
        print("\n1. Adaugă o carte")
        print("2. Afișează toate cărțile")
        print("3. Șterge o carte")
        print("4. Caută cărți")
        print("5. Ieșire")
        choice = input("Alege o opțiune: ")

        if choice == "1":
            # Cod pentru adăugare carte
            pass
        elif choice == "2":
            # Cod pentru afișare cărți
            pass
        elif choice == "3":
            # Cod pentru ștergere carte
            pass
        elif choice == "4":
            # Cod pentru căutare carte
            pass
        elif choice == "5":
            break
        else:
            print("Opțiune invalidă!")


if __name__ == "__main__":
    main()
