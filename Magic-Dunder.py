#These are special methods you can define in your classes, and when invoked
#They give you a powerful way to manipulate object and their behaviour
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

book1 = Book("Harry Potter", "J.K. Rowling")

print(book1)         
print(len(book1))      
