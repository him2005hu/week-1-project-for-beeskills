# Student Library Management System

class Library:

    def __init__(self, books):
        self.books = books
        self.borrowed_books = {}

    def display_books(self):
        print("\nAvailable Books:")

        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            print("-", book)

    def borrow_book(self, book_name, student_name):

        if book_name in self.books:
            self.books.remove(book_name)

            self.borrowed_books.setdefault(
                book_name, []
            ).append(student_name)

            print(student_name, "borrowed", book_name)
            return True

        else:
            print("Sorry! Book is not available.")
            return False

    def return_book(self, book_name, student_name):

        borrowers = self.borrowed_books.get(
            book_name, []
        )

        if student_name in borrowers:

            borrowers.remove(student_name)

            if not borrowers:
                del self.borrowed_books[book_name]

            self.books.append(book_name)

            print(student_name, "returned", book_name)
            return True

        else:
            print("You have not borrowed this book.")
            return False


class Student:

    def __init__(self, name, library):
        self.name = name
        self.library = library
        self.borrowed_books = []

    def borrow(self, book_name):

        if self.library.borrow_book(
            book_name, self.name
        ):
            self.borrowed_books.append(book_name)

    def return_book(self, book_name):

        if self.library.return_book(
            book_name, self.name
        ):
            self.borrowed_books.remove(book_name)

    def show_my_books(self):

        if not self.borrowed_books:
            print("You have not borrowed any books.")

        else:
            print("\nYour Borrowed Books:")

            for book in self.borrowed_books:
                print("-", book)


def main():

    books = [
        "Python Programming",
        "Introduction to AI",
        "Business Analytics",
        "Data Science Basics",
        "Computer Networks"
    ]

    library = Library(books)

    name = input("Enter student name: ").strip()

    if not name:
        name = "Student"

    student = Student(name, library)

    while True:

        print("\n===== Student Library Menu =====")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show my borrowed books")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            library.display_books()

        elif choice == "2":

            library.display_books()

            book = input(
                "Enter book name to borrow: "
            ).strip()

            student.borrow(book)

        elif choice == "3":

            student.show_my_books()

            book = input(
                "Enter book name to return: "
            ).strip()

            student.return_book(book)

        elif choice == "4":

            student.show_my_books()

        elif choice == "5":

            print("Thank you for using the Library System!")
            break

        else:

            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()