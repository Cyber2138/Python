class library:
    def __init__(self):
        self.number_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.number_of_books = len(self.books)

    def info(self):
        print(f"The total books in the library are {self.number_of_books}\nThe available books are ")
        for self.book in self.books:
            print(self.book)

b1 = library()
b1.add_book('shadow Fighter')
b1.add_book("Harry potter")
b1.info()
