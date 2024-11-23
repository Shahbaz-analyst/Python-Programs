# Library Management System

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
        
    def addBook(self, args):
        self.books.append(args)
        self.noBooks = len(self.books)
    
    def showInfo(self):
        print(f"The number of books present in Library are: {self.noBooks} \nThe Books are:")
        for book in self.books:
            print(book)
        
l1 = Library()
l1.addBook("Harry Puttar")
l1.addBook("Atomic Habits")
l1.addBook("Alis in Wonderland")
l1.addBook("Kindergarten")
Library.showInfo(l1)
