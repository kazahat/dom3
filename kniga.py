class Book:
    def __init__(self, name, author, year, genre = "Не определен"):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
    def info(self):
        print(f"Название:{self.name} Автор:{self.author} Год:{self.year} Жанр: {self.genre}")


b = Book("Война и мир", "Л.Н.Толстой", 1865, "Роман")
b.info()

