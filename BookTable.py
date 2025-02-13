class BookTable:
    def __init__(self):
        # Initialize an empty list to simulate a database table
        self.books = []

    def add_book(self, title, author, isbn):
        """
        Add a new book to the table.
        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN of the book
        """
        book = {
            "title": title,
            "author": author,
            "isbn": isbn
        }
        self.books.append(book)
        print(f"Book '{title}' by {author} added successfully.")

    def list_books(self):
        """
        List all books in the table.
        """
        if not self.books:
            print("No books found.")
        else:
            print("List of Books:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

    def find_book_by_isbn(self, isbn):
        """
        Find a book by its ISBN.
        :param isbn: ISBN of the book to find
        :return: The book if found, otherwise None
        """
        for book in self.books:
            if book["isbn"] == isbn:
                return book
        return None

    def delete_book_by_isbn(self, isbn):
        """
        Delete a book by its ISBN.
        :param isbn: ISBN of the book to delete
        """
        book = self.find_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            print(f"Book '{book['title']}' by {book['author']} deleted successfully.")
        else:
            print(f"No book found with ISBN: {isbn}")
if __name__ == "__main__":
    book_table = BookTable()
    book_table.add_book("Pride and Prejudice", "Jane Austen", "1234567891234")
    book_table.add_book("The Catcher in the Rye", "J.D. Salinger", "0000000000001")
    book_table.list_books()
    found_book = book_table.find_book_by_isbn("1234567891234")
    if found_book:
        print(f"Found book: {found_book['title']} by {found_book['author']}")
    book_table.delete_book_by_isbn("1234567891234")
    book_table.list_books()
