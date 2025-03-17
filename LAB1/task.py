# TODO: Подробно описать три произвольных класса
import doctest
# TODO: описать класс

class movie:
    def __init__(self, name: str = None, rating: int = None):
        '''
        Создание и подготовка к работе объекта "Фильм"
        :param name: Название фильма
        :param rating: Рейтинг фильма
        '''

        self.name = name
        self.rating = rating
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен быть типа int или float")
        if rating < 0:
            raise ValueError("Рейтинг не может быть ниже нуля")

    def is_it_worth_watching(self):
        if self.rating > 75:
            print("Стоит")
        else:
            print ("Возможно, не стоит")

    def print_info(self):
        print(self.name,"--->", self.rating)


#Z = movie("ЗЕТ", 80)
#Z.is_it_worth_watching()
#Z.print_info()


# TODO: описать ещё класс

class music:
    def __init__(self, name: str = None, dur_in_secs: int = None, Tima_Belorusskih: bool = False):
        '''
        Создание и подготовка к работе объекта "Песня"
        :param name: Название песни
        :param dur_in_secs: Длительность в секундах песни
        :param Tima_Belorusskih: Является ли Тима Белорусских автором этой песни?
        '''

        self.name = name
        self.dur_in_secs = dur_in_secs
        self.Tima_Belorusskih = Tima_Belorusskih
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if not isinstance(dur_in_secs, int):
            raise TypeError("Длительность должна быть типа int")
        if dur_in_secs < 0:
            raise ValueError("Длительность не может быть ниже нуля")
        if not isinstance(Tima_Belorusskih, bool):
            raise TypeError("Является ли Тима Белорусских автором этой песни должно быть типа bool")

    def Tima(self):
        if self.Tima_Belorusskih == True:
            print("Песня топ")

    def print_info(self):
        print(self.name, self.dur_in_secs)


#Nez = music("Незабудка", 323, True)
#Nez.Tima()
#Nez.print_info()


# TODO: и ещё один

class game:
    def __init__(self, name: str = None, rating: int = None):
        '''
        Создание и подготовка к работе объекта "Игра"
        :param name: Название игры
        :param rating: Рейтинг игры
        '''

        self.name = name
        self.rating = rating
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен быть типа int или float")
        if rating < 0:
            raise ValueError("Рейтинг не может быть ниже нуля")

    def is_it_worth_playing(self):
        if self.rating > 75:
            print("Стоит")
        else:
            print ("Возможно, не стоит")

    def print_info(self):
        print(self.name,"--->", self.rating)

if __name__ == "__main__":
    doctest.testmod()

#Dota = game("DotA 2", 100)
#Dota.is_it_worth_playing()
#Dota.print_info()