import json

def load_books(library):
    with open("books.json") as f:
        bookList = json.load(f)

    # print(bookList)
    # print(type(bookList))

    for book in bookList:
        # print(book['title'])
        # print(book['author'])
        # print(book['price'])
        # print(book['publishDate'])
        # print(book['onLoan'])
        library.add_book(book['title'], book['author'], book['price'], book['publishDate'], book['onLoan'])