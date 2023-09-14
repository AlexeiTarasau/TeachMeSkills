class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_author(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

book1 = Book("War and peace", "Ley Tolstoy", 1869)
book2 = Book("Crime and Punishment", "Fedor Dostoeysky", 1866)
book3 = Book("1984", "George Orwell", 1949)

print(f"Book 1: Name - {book1.get_title()}, Author - {book1.get_author()}, The year of publishing - {book1.get_year()}")
book1.set_year(1871)
print(f"Updated year of publication of the book 1: {book1.get_year()}")

print(f"Book 2: Name - {book2.get_title()}, Author - {book2.get_author()}, The year of publishing - {book2.get_year()}")
book2.set_title("Crime and Punishment (Dostoeysky)")
print(f"Updated year of publication of the book 2: {book2.get_title()}")

print(f"Book 3: Name - {book3.get_title()}, Author - {book3.get_author()}, The year of publishing - {book3.get_year()}")
book3.set_author("George Orwell")
print(f"Updated year of publication of the book 3: {book3.get_author()}")
