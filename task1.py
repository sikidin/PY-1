class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name() #возвращает название книги

    @name.setter
    def name(self, name: str) -> None:
        self._name = name #Устанавливает название книги

    @property
    def author(self) -> str:
        return self._author() #возвращает имя автора

    @author.setter
    def author(self, author: str) -> None:
        self._author = author #Устанавливает имя автора

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int):
        super().__init__()
        self._pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, duration: float):
        super().__init__()
        self._duration = duration

    @property
    def duration(self) -> int:
        """Возвращает продолжительность книги."""
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Устанавливает продолжительность книги."""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги  должно быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность книги должно быть положительным числом")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

