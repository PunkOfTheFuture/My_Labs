class Book:
    """ Базовый класс книги. """

    __name = None
    __author = None


    def __init__(self, __name: str, __author: str):
        self.name = __name
        self.author = __author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.pages = pages
        if not isinstance(pages, int):
            raise TypeError
        super().__init__(name, author)


    def __str__(self):
        return super().__str__() + f' количество страниц: {self.pages}'



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.duration = duration
        if not isinstance(duration, float):
            raise TypeError
        super().__init__(name, author)


    def __str__(self):
        return super().__str__() + f' длительность: {self.duration}'

