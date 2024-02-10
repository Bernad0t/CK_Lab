class Games:
    """Описание игры: название, издательство, дата выхода"""
    GENRE = 'игра'

    def __init__(self, name: str, publisher: str, release: int):
        self.name = name
        self.publisher = publisher
        self._release = release  # компьютерные игры существуют с 1962 года

    @property
    def release(self):
        return self._release

    @release.setter
    def release(self, release):
        if release < 1962:
            raise ValueError
        self.release = release

    def __str__(self):
        return f"{self.GENRE} {self.name} издана в {self.release} компанией {self.publisher}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.publisher}', {self.release})"


class StrategyGame(Games):
    """Описание игры в жанре стратегии: название, издательство, дата выхода,
    способ игры (пошаговая или в реальном времени)"""
    GENRE = 'стратегия'

    def __init__(self, name: str, publisher: str, release: int, view: str):
        """Унаследовывается у класса Games задание атрибутов name,
        publisher, release и добавляется новый атрибут view в связи с
        особенностью жанра"""
        super().__init__(name, publisher, release)
        self.view = view  # пошаговая/в реальном времени/в реальном времени с пошаговыми элементами

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.publisher}', {self.release}, {self.view})"


if __name__ == "__main__":
    # Write your solution here
    TW = StrategyGame('Сёгун тотал вар', 'SEGA', 1998, 'в реальном времени с пошаговыми элементами')
    print(TW)
    print(repr(TW))
