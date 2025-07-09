class Library:
    def __init__(self):
        self.nameOfBooks = []
        self.noOfBooks = 0

    def addBook(self, bookName):
        self.nameOfBooks.append(bookName)
        self.noOfBooks += 1

    def noofbooks(self):
        if self.nameOfBooks:
            print("Books in library:")
            for book in self.nameOfBooks:
                print(f"- {book}")
        else:
            print("No books in the library.")

    def getBooks(self):
        return self.noOfBooks

o = Library()
o.addBook("The Alchemist")
o.addBook("To Kill a Mockingbird")
o.addBook("Gitanjali")
o.noofbooks()
print("Total number of books:", o.getBooks())
