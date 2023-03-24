class Book:
    def __init__(self, title, author, publisher, genre, year, code):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.year = year
        self.code = code


class Library:
    def __init__(self):
        self.books = []

    def view_books(self):
        print("List of Books:")
        for book in self.books:
            print(
                f"Title: {book.title}, Author: {book.author}, Publisher: {book.publisher}, Genre: {book.genre}, Year: {book.year}, code: {book.code}")

    def add_book(self, book):
        self.books.append(book)
        print("Book added to the library")

    def update_book(self, code):
        for book in self.books:
            if book.code == code:
                book.title = input("Enter new title: ")
                book.author = input("Enter new author: ")
                book.publisher = input("Enter new publisher: ")
                book.genre = input("Enter new genre: ")
                book.year = input("Enter new year: ")
                print("Book information updated")
                return
        print("Book not found")

    def remove_book(self, code):
        for book in self.books:
            if book.code == code:
                self.books.remove(book)
                print("Book information removed")
                return
        print("Book not found")

    def search_book(self, keyword):
        result = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.genre.lower():
                result.append(book)
        if len(result) == 0:
            print("No book found")
        else:
            print("Search result:")
            for book in result:
                print(
                    f"Title: {book.title}, Author: {book.author}, Publisher: {book.publisher}, Genre: {book.genre}, Year: {book.year}, code: {book.code}")

    def sort_books(self, sort_by):
        if sort_by == "title":
            self.books.sort(key=lambda x: x.title)
        elif sort_by == "author":
            self.books.sort(key=lambda x: x.author)
        elif sort_by == "publisher":
            self.books.sort(key=lambda x: x.publisher)
        elif sort_by == "genre":
            self.books.sort(key=lambda x: x.genre)
        elif sort_by == "year":
            self.books.sort(key=lambda x: x.year)
        else:
            print("Invalid sort option")
            return
        print("Books sorted")


library = Library()

book1 = Book("Book 1", "Author 1", "Publisher 1", "Fiction", 1960, "1")
book2 = Book("Book 2", "Author 2", "Publisher 2", "Fiction", 1951, "2")
book3 = Book("Book 3", "Author 3", "Publisher 3", "Fiction", 1967, "3")
book4 = Book("Book 4", "Author 4", "Publisher 4", "Fiction", 1949, "4")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)


def menu():
    print("LIBRARY APPLICATION MENU\n")
    print("1. View all books")
    print("2. Add new book")
    print("3. Update book information")
    print("4. Remove book")
    print("5. Search for a book")
    print("6. Sort books")
    print("0. Exit")

    # Get the user's choice
    choice = input("\nEnter your choice: ")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        library.view_books()
    elif choice == "2":
        book = Book(input("Enter the book title: "),
                    input("Enter the book author: "),
                    input("Enter the book publisher: "),
                    input("Enter the book genre: "),
                    input("Enter the book year: "),
                    input("Enter the book code: "))
        library.add_book(book)
    elif choice == "3":
        code = input("Enter the code of the book to update: ")
        library.update_book(code)
    elif choice == "4":
        code = input("Enter the code of the book to remove: ")
        library.remove_book(code)
    elif choice == "5":
        keyword = input("Enter the keyword to search for: ")
        library.search_book(keyword)
    elif choice == "6":
        sort_by = input("Enter the field to sort by (title, author, publisher, genre, year, code): ")
        library.sort_books(sort_by)
    elif choice == "0":
        exit()
    else:
        print("Invalid choice. Please try again.\n")

    # Gọi lại hàm menu để người dùng tiếp tục sử dụng chương trình
    menu()


menu()
