# Digital Library Management System

A simple Python-based console application for managing book borrowing and returning in a digital library.

## Description

This project simulates a basic library management system where users can:

- View available books
- Issue (borrow) books
- Return books
- Track their issued books

The system maintains an inventory of books with multiple copies and tracks which books are currently issued to each user.

## Features

- User registration with name and registration number
- Predefined book inventory with multiple copies
- Interactive menu system
- Book issuing and returning functionality
- Real-time inventory updates
- User-specific book tracking
- Input validation and error handling

## Requirements

- Python 3.x

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Download or clone the repository.
3. Navigate to the project directory.
4. Run the script using:

```bash
python lib.py
```

## Usage

1. Start the program by running `lib.py`.
2. Enter your name and registration number when prompted.
3. Choose from the menu options:
   - **1. Issue a book**: Select from available books to borrow.
   - **2. Submit a book**: Return a previously issued book.
   - **3. View available books**: See current inventory.
   - **4. Exit**: Quit the application.
4. Follow the on-screen prompts to complete your actions.

## Book Inventory

The system comes with a predefined set of books:

- Python Programming (10 copies)
- Data Structures (5 copies)
- Machine Learning (8 copies)
- Web Development (12 copies)
- Database Systems (6 copies)
- Artificial Intelligence (4 copies)
- Cybersecurity (7 copies)
- Cloud Computing (9 copies)

## Limitations

- Data is not persisted between runs (in-memory only)
- No user authentication beyond name and registration number
- Fixed book inventory (not dynamically manageable)

## Contributing

Feel free to fork this repository and submit pull requests with improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
