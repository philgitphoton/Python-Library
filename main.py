from library import Library
import books
import jsonReader


library = Library()
# books.load_books(library)
jsonReader.load_books(library)

while True:
    print("\n")
    print("---------------------------")
    print("Welcome to the Library")
    print("---------------------------")
    print("What would you like to do")
    print("0. Add a book to the library")
    print("1. See all books in the library")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    print("---------------------------")
    print("\n")

    choice = input()
    print("\n")

    if choice == "0":
        books.add_book(library)
    if choice == "1":    
        books.list_books(library)
    if choice == "2":
        books.borrow_book(library)
    if choice == "3":
        books.return_book(library)
    if choice == "4":
        books.commit(library)
        break