import doctest


class Factory:
    def __init__(self, performance_shift_1: int, performance_shift_2: int, performance_shift_3: int):

        """
        Создание и подготовка к работе объекта "Фабрика"

        :param performance_shift_1: Выработка первой смены
        :param performance_shift_2: Выработка второй смены
        :param performance_shift_3: Выработка третьей смены

        Примеры:
        >>> performance = Factory(1000, 800, 1300)  # инициализация экземпляра класса
        """

        if not isinstance(performance_shift_1, int):
            raise TypeError("Выработка смены должна быть типа int")
        if performance_shift_1 <= 0:
            raise ValueError("Выработка смены должна быть положительным числом")
        self.performance_shift_1 = performance_shift_1

        if not isinstance(performance_shift_2, int):
            raise TypeError("Выработка смены должна быть типа int")
        if performance_shift_2 <= 0:
            raise ValueError("Выработка смены должна быть положительным числом")
        self.performance_shift_2 = performance_shift_2

        if not isinstance(performance_shift_3, int):
            raise TypeError("Выработка смены должна быть типа int")
        if performance_shift_3 <= 0:
            raise ValueError("Выработка смены должна быть положительным числом")
        self.performance_shift_3 = performance_shift_3

    def overall_performance(self) -> int:

        """
        Функция которая показывает общую выработку смен за день

        :return: 3100

        Примеры:
        >>> performance = Factory(1000, 800, 1300)
        >>> performance.overall_performance()
        """
    ...

    def best_shift(self) -> str:
        """
        Функция которая показывает лучшую смену по выработке за день

        :return: "Лучшая смена за день 3!"

        Примеры:
        >>> performance = Factory(1000, 800, 1300)
        >>> performance.best_shift()
        """
    ...


class Deck:
    def __init__(self, cards: int, players: int, draw: int):

        """
        Создание и подготовка к работе объекта "Колода"

        :param cards: Колличество карт в колоде
        :param players: Колличество игроков
        :param draw: Колличество карт на раздаче одному игроку

        Примеры:
        >>> game = Deck(52, 3, 5)  # инициализация экземпляра класса
        """

        if not isinstance(cards, int):
            raise TypeError("Количество карт в колоде должно быть типа int")
        if cards <= 0:
            raise ValueError("Количество карт в колоде должно быть положительным числом")
        self.cards = cards

        if not isinstance(players, int):
            raise TypeError("Количество игроков должно быть типа int")
        if players <= 0:
            raise ValueError("Количество игроков должно быть положительным числом")
        self.players = players

        if not isinstance(draw, int):
            raise TypeError("Количество карт на раздаче одному игроку должyj быть типа int")
        if draw <= 0:
            raise ValueError("Количество карт на раздаче одному игроку должyj быть положительным числом")
        self.draw = draw

    def cards_balance(self) -> int:
        """
        Функция которая показывает остаток карт в колоде

        :return: 37

        Примеры:
        >>> game = Deck(52, 3, 5)
        >>> game.cards_balance()
        """
        ...

    def cards_out(self) -> int:
        """
        Функция которая показывает количество карт вне игры

        :return: 15

        Примеры:
        >>> game = Deck(52, 3, 5)
        >>> game.cards_out()
        """
        ...


class Library:
    def __init__(self, books: int, books_out: int):

        """
        Создание и подготовка к работе объекта "Библиотека"

        :param books: Всего книг в библиотеке
        :param books_out: Количество выданных книг

        Примеры:
        >>>  number_books= Library(1000, 287)  # инициализация экземпляра класса
        """

        if not isinstance(books, int):
            raise TypeError("Количество книг в библиотеке должно быть типа int")
        if books <= 0:
            raise ValueError("Количество книг в библиотеке должно быть положительным числом")
        self.books = books

        if not isinstance(books_out, int):
            raise TypeError("Количество выданных книг  должно быть типа int")
        if books_out <= 0:
            raise ValueError("Количество выданных книг должно быть положительным числом")
        self.books_out = books_out

    def rest_books(self) -> int:
        """
        Функция которая показывает количество книг которые остались в библиотеке

        :return: 713

        Примеры:
        >>> number_books = Library(1000, 287)
        >>> number_books.rest_books()
        """
        ...

    def rest_books_1(self, books_return: int) -> int:
        """
        Функция которая показывает количество книг которые остались в библиотеке после возврата книг
        :param books_return: Количество вернувшихся книг

        :raise ValueError: Если количество вернувшихся книг больше больше количества выданных, то вызываем ошибку

        :return: 802

        Примеры:
        >>> number_books = Library(1000, 287)
        >>> number_books.rest_books_1(89)
        """
        if not isinstance(books_return, int):
            raise TypeError("Количество вернувшихся книг должно быть типа int")
        if books_return <= self.books_out:
            raise ValueError("Количество вернувшихся книг больше выданных книг")
        ...



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации