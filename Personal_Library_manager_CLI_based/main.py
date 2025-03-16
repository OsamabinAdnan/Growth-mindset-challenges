import json  # Import the json module to handle JSON file operations

# Class is a printer and it creates a blueprint of object and methods, object is like a page, and on that page we have some kind of data
# We store that data on page (object) and we used different methods on that object, methods perform some kinds of action within the object
# Methods are generally functions but they are inside class that why we call them methods
class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """
        Initialize a new book collection with an empty list and set up file storage.
        'self' refers to the instance of the class. It allows each method to access and modify the attributes of the specific object created from this class.
        """
        self.book_list = []  # Initialize an empty list to store books
        self.storage_file = "book_data.json"  # Define the filename for storing book data
        self.read_from_file()  # Load any existing books from file
    
    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:  # Try to open and read the JSON file
                self.book_list = json.load(file)  # Load JSON data into book_list
        except(FileNotFoundError, json.JSONDecodeError):
            self.book_list = []  # If file doesn't exist or is corrupted, start with empty list
    
    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:  # Open file in write mode
            json.dump(self.book_list, file, indent=4)  # Save book_list as formatted JSON
    
    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter the title of the book: ")  # Get book title from user
        book_author = input("Enter the author of the book: ")  # Get book author from user
        publication_year = input("Enter the publication year of the book: ")  # Get publication year from user
        book_genre = input("Enter the genre of the book: ")  # Get book genre from user
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"  # Convert yes/no input to boolean
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)  # Add book to collection
        self.save_to_file()  # Save updated collection to file
        print(f"\nBook '📗{book_title}' added to the collection.")
    
    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")  # Get book title to delete

        for book in self.book_list:  # Search for book in collection
            if book["title"].lower() == book_title.strip().lower():  # If book found
                self.book_list.remove(book)  # Remove book from collection
                self.save_to_file()  # Save updated collection to file
                print(f"\nBook '📕{book_title}' removed from the collection.")
                return
        
        print(f"Book '📕{book_title}' not found in the collection.")  # Book not found message
    
    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search book by:\n1. Title\n2. Author\nEnter your choice: ")  # Get search preferences
        search_text = input("Enter search term to search the book (title/author name):").strip().lower()  # Get search term

        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()  # Find matching books by title
            or search_text in book["author"].lower()  # Find matching books by author
        ]

        if found_books:  # If books found
            print(f"Found {len(found_books)} books matching '{search_text}'")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"  # Determine reading status
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Has been read: {reading_status}"
                )
        else:
            print(f"\nNo books found matching '{search_text}'")  # No books found message
    
    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book to update:")  # Get book to update
        for book in self.book_list:  # Find book in collection
            if book["title"].lower() == book_title.strip().lower():  # If book found
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}):") or book["title"]  # Update title
                book["author"] = input(f"New author ({book['author']}):") or book["author"]  # Update author
                book["year"] = input(f"New publication year ({book['year']}):") or book["year"]  # Update year
                book["genre"] = input(f"New genre ({book['genre']}):") or book["genre"]  # Update genre
                book["read"] = input(f"Have you read this book? (yes/no): ").strip().lower() == "yes"  # Update read status
                
                self.save_to_file()  # Save updated collection to file
                print(f"Book '📙 {book_title}' updated successfully.")
                return
        print(f"\nBook '📙 {book_title}' not found in the collection.")  # Book not found message

    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.book_list:  # Check if collection is empty
            print("\nNo books found in the collection. Your collection is empty\n")
            return
        
        print("\n📚 All Books in the Collection:\n")
        for index, book in enumerate(self.book_list, 1):  # Print all books
            reading_status = "Read" if book["read"] else "Unread"  # Determine reading status
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Has been read: {reading_status}"
            )
        print()
    
    def showing_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)  # Calculate total books
        completed_books = sum(1 for book in self.book_list if book["read"])  # Calculate completed books
        completed_rate = (
            (completed_books / total_books) * 100 if total_books > 0 else 0  # Calculate completion rate
        )
        print(f"\n📊 Reading Progress:\n")
        print(f"Total Books in Collection: {total_books}")
        print(f"Reading Progress: {completed_rate:.2f}%\n")
    
    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("\n📚 Welcome to Your Book Collection Manager! 📚\n")
            print("1. Add a new book")
            print("2. Delete/Remove a book")
            print("3. Search for a book")
            print("4. Update book details")
            print("5. View all books in the collection")
            print("6. View Reading progress")
            print("7. Exit")
            user_choice = int(input("Please choose an option (1-7): "))  # Get user choice

            if user_choice == 1:
                self.create_new_book()  # Call create_new_book method
            elif user_choice == 2:
                self.delete_book()  # Call delete_book method
            elif user_choice == 3:
                self.find_book()  # Call find_book method
            elif user_choice == 4:
                self.update_book()  # Call update_book method
            elif user_choice == 5:
                self.show_all_books()  # Call show_all_books method
            elif user_choice == 6:
                self.showing_reading_progress()  # Call showing_reading_progress method
            elif user_choice == 7:
                self.save_to_file()  # Save collection to file
                print("\nExiting the application. Thank you for using Book Collection Manager! Goodbye! 👋")
                break  # Exit the loop
            else:
                print("\nInvalid choice. Please select a valid option (1-7).")  # Invalid choice message


if __name__ == "__main__":
    book_manager = BookCollection()  # Create instance of BookCollection
    book_manager.start_application()  # Start the application
