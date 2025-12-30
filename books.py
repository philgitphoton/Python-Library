from library import Library

all_books=[]

library = Library()

def load_books():
    library.add_book("1984", "George Orwell", 9.99, "1949-06-08", False)
    library.add_book("The Hobbit", "J.R.R. Tolkien", 12.50, "1937-09-21", True)
    library.add_book("Dune", "Frank Herbert", 15.00, "1965-08-01", False)

def list_books():    
    all_books = library.get_all_books()
    for index, book in enumerate(all_books):
        print(index, book)
        
def borrow_book():
    all_books = library.get_all_books()
    print("\n" + "Books that are available to borrow:")
    for index, book in enumerate(all_books):
        if not book[4]:
            print(index, book)
    choice = int(input ("\n" + "What book number would you like to borrow? "))
    book = all_books[choice]
    if not book[4]:
        book[4] = True
        print("\n" + "You have checked out: ", book)
    else:
        print("\n" + "That book is already on loan")

def return_book():
    all_books = library.get_all_books()
    title = input ("\n" + "Enter the title of the book you would like to return: ")
    for index, book in enumerate(all_books):
        if title == book[0]:
            if book[4] == True:
                print("Return accepted")
                break
            else:
                print("\n" + "That book is not currently on loan")
                break
        if not title == book[0]:
            print("\n" + "We don't have that book, or you have mistyped the title")
            return