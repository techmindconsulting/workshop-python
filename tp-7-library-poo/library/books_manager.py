class BooksManager():
    def __init__(self, books_loader):
        if isinstance(books_loader, BooksLoader):
            self.books = books_loader.load()

    def add_film(self, book):
        if isinstance(book, Book):
            self.books.append(book)

# A completer
