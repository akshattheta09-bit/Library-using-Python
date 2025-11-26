print("Welcome to the Digital Library Management System")
print()
print()
print("You can borrow or return any book of your desire.")
print("We have a wide collection of books available.")
print()

name = input("For information purposes, kindly type your name: ").strip().title()
registration_number = input("Kindly type your registration number: ").strip()
try:
    reg_num = int(registration_number)
    print(f"\nHello, {name}! Your registration number is {reg_num}.")
except ValueError:
    print("\nInvalid registration number. Please enter a numeric value.")
    exit()

print()


books = {
    "Python Programming": 10,
    "Data Structures": 5,
    "Machine Learning": 8,
    "Web Development": 12,
    "Database Systems": 6,
    "Artificial Intelligence": 4,
    "Cybersecurity": 7,
    "Cloud Computing": 9
}

total_books = sum(books.values())
print(f"Total number of books available in the library: {total_books}")
print("\nAvailable books:")
for book, count in books.items():
    print(f"- {book}: {count} copies")

print()

print("Options:")
print("1. Issue a book")
print("2. Submit a book")
print("3. View available books")
print("4. Exit")

issued_books = {}

while True:
    try:
        choice = input("\nPlease select an option (1-4): ").strip()
        if choice == "1":

            print("\nAvailable books to issue:")
            for i, (book, count) in enumerate(books.items(), 1):
                if count > 0:
                    print(f"{i}. {book} ({count} copies available)")
            book_choice = input("Enter the number of the book you want to issue: ").strip()
            try:
                book_index = int(book_choice) - 1
                book_list = list(books.keys())
                if 0 <= book_index < len(book_list):
                    selected_book = book_list[book_index]
                    if books[selected_book] > 0:
                        books[selected_book] -= 1
                        if name not in issued_books:
                            issued_books[name] = []
                        issued_books[name].append(selected_book)
                        print(f"\nBook '{selected_book}' issued successfully to {name}.")
                        print(f"Remaining copies: {books[selected_book]}")
                    else:
                        print(f"\nSorry, '{selected_book}' is currently out of stock.")
                else:
                    print("\nInvalid book selection.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

        elif choice == "2":

            if name in issued_books and issued_books[name]:
                print(f"\nBooks issued by {name}:")
                for i, book in enumerate(issued_books[name], 1):
                    print(f"{i}. {book}")
                return_choice = input("Enter the number of the book you want to return: ").strip()
                try:
                    return_index = int(return_choice) - 1
                    if 0 <= return_index < len(issued_books[name]):
                        returned_book = issued_books[name].pop(return_index)
                        books[returned_book] += 1
                        print(f"\nBook '{returned_book}' returned successfully.")
                        print(f"Updated copies: {books[returned_book]}")
                        if not issued_books[name]:
                            del issued_books[name]
                    else:
                        print("\nInvalid book selection.")
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
            else:
                print(f"\n{name}, you have no books to return.")

        elif choice == "3":
            print("\nCurrent available books:")
            total_books = sum(books.values())
            print(f"Total books: {total_books}")
            for book, count in books.items():
                print(f"- {book}: {count} copies")

        elif choice == "4":
          
            print(f"\nThank you for using the Digital Library, {name}!")
            if name in issued_books:
                print(f"You have the following books issued: {', '.join(issued_books[name])}")
                print("Please return them when possible.")
            break

        else:
            print("\nInvalid option. Please choose 1, 2, 3, or 4.")

    except KeyboardInterrupt:
        print("\n\nOperation interrupted. Exiting...")
        break
    except Exception as e:
        print(f"\nAn error occurred: {e}. Please try again.")

print("\nHave a great day!")


