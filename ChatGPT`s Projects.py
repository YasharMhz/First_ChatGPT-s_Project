class Book:
    def __init__(self, title, author, year, genre, is_borrowed):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_borrowed = is_borrowed

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"title = {book.title} , author = {book.author} , year = {book.year} ")

    def search_book(self,title):
        found = False

        for book in self.books:
            if book.title == title:
                print(book.title)
                found = True

        if not found:
            print("Book not found")


    def remove_book(self,title):
        found = False

        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                found = True

        if not found:
            print("Book not found")

my_library = Library()

while True :
    print("""1- Add Book
    2- Show Books
    3- Search
    4- Remove
    5- Exit """)
    x = input("enter your option : ")
    if x.title() == "Exit" :
        break







bookFirst = Book("book 1","person 1",1990,"romantic",False)
bookSecond = Book("book 2","person 2",2000,"action",False)
bookThird = Book("book 3","person3",2001,"romantic",False)


my_library.add_book(bookFirst)

my_library.show_books()
my_library.search_book("book 1")

my_library.remove_book("book 2")

my_library.show_books()