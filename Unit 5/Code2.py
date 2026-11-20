
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"name": book, "issued": False})
        print("Book added successfully.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\n--- BOOK LIST ---")
            for book in self.books:
                status = "Issued" if book["issued"] else "Available"
                print("Book:", book["name"], "| Status:", status)

    def issue_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                if not book["issued"]:
                    book["issued"] = True
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                if book["issued"]:
                    book["issued"] = False
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


# Main Program
library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice.")
