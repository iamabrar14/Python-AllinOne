class Books:
    def __init__(self, initial_book=0):
        self.books = initial_book

    def save(self, addBook):
        self.books += addBook
        print(f"Added: {addBook}")
        print(f"Books: {self.books}")

    def borrow(self, borrowBook):
        if borrowBook <= self.books:
            self.books -= borrowBook
            print(f"Borrowed: {borrowBook}")
            print(f"Books remaining: {self.books}")
        else:
            print(f"Not enough books to borrow. Only {self.books} available.")


library = Books(10)
library.save(5)
library.borrow(3)
library.borrow(20)
