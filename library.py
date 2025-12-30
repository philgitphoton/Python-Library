class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, price, publishDate, onLoan):
        self.books.append([title, author, price, publishDate, onLoan])

    def get_all_books(self):
        return list(self.books)