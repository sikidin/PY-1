import doctest


class Bridges:
    def __init__(self, number_supports: int, length: int):

        """
        Базовый класс Мосты
        Создание и подготовка к работе объекта "Мосты"

        :param number_supports: Количество опор моста
        :param length: Длина моста

        Примеры:
        >>> bridge = Bridges(5, 120)  # инициализация экземпляра класса
        """

        if not isinstance(number_supports, int):
            raise TypeError("Количество опор должно быть типа int")
        if number_supports <= 0:
            raise ValueError("Количество опор должно быть положительным числом")
        self.number_supports = number_supports

        if not isinstance(length, int):
            raise TypeError("Длина моста должна быть типа int")
        if length <= 0:
            raise ValueError("Длина моста должна быть положительным числом")
        self.length = length

    def __str__(self):
        return f"Мост имеет {self.number_supports} опор. Длина моста {self.length} м."

    def __repr__(self):
        return f"{self.__class__.__name__}(number_supports={self.number_supports!r}, length={self.length!r})"

    def span_length(self) -> int:
        """
        Функция которая показывает длину одного пролета

        :return: 30

        Примеры:
        >>> bridge = Bridges(5, 120)  # инициализация экземпляра класса
        >>> bridge.span_length()
        """
    ...

    def materials_bridge(self, material_supports: str) -> str:
        """
        Функция которая показывает материалы из которых изготовлены конструкции моста

        :param material_supports: Материал из которого изготовлены опоры

        :return: "Опоры изготовлены из бетона"

        Примеры:
        >>> bridge = Bridges(5, 120)
        >>> bridge.materials_bridge('Бетон')
        """

    ...


class Cable_Stayed_Bridge(Bridges):
    def __init__(self, number_supports: int, length: int, length_cable_stayed: float):
        super().__init__(number_supports, length)

        """
        Дочерний класс Вантовый мост
        Создание и подготовка к работе объекта "Вантовый мост"

        :param length_cable_stayed: Длина ванта

        Примеры:
        >>> bridge = Cable_Stayed_Bridge(5, 120, 68.2)  # инициализация экземпляра класса
        """

        if not isinstance(length_cable_stayed, float):
            raise TypeError("Длина ванта должна быть типа float")
        if length_cable_stayed <= 0:
            raise ValueError("Длина ванта должна быть положительным числом")
        self.length_cable_stayed = length_cable_stayed

    def __repr__(self):
        return f"{self.__class__.__name__}(number_supports={self.number_supports!r}, length={self.length!r}, \
               length_cable_stayed={self.length_cable_stayed!r})"

    def materials_bridge(self, material_supports: str, material_cable_stayed: str) -> str:

        super().materials_bridge(material_supports)

        """
        Функция которая показывает материалы из которых изготовлены конструкции моста
        
        Перегружаем метод добавляя материал ванта 
        
        :param material_supports: Материал из которого изготовлены опоры
        :param material_cable_stayed: Материал из которого изготовлены ванты

        :return: "Опоры изготовлены из бетона. Ванты изготовлены из стали"

        Примеры:
        >>> bridge = Bridges(5, 120, 68.2)
        >>> bridge.materials_bridge("Бетон", "Сталь")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
