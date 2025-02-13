class BookModel:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, year={self.publication_year})"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "publication_year": self.publication_year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            isbn=data.get("isbn"),
            publication_year=data.get("publication_year")
        )
if __name__ == "__main__":
    book = BookModel(
        title="Die Farben der Liebe",
        author=" marten lother",
        isbn="978-3-16-37658-02",
        publication_year=2025
    )
    print(book)
    book_dict = book.to_dict()
    print(book_dict)
    new_book = BookModel.from_dict(book_dict)
    print(new_book)