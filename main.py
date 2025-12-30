import books

books.load_books()
3
while True:
    print("\n")
    print("---------------------------")
    print("Welcome to the Library")
    print("---------------------------")
    print("What would you like to do")
    print("1. See all books in the library")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    print("---------------------------")
    print("\n")

    choice = input()
    print("\n")

    if choice == "1":    
        books.list_books()
    if choice == "2":
        books.borrow_book()
    if choice == "3":
        books.return_book()