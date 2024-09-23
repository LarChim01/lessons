#Дополнительное практическое задание по модулю: "Наследование классов."
import math

pi = math.pi  # число пи


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.set_sides_f(*sides)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r) and self.__is_valid_color(g) and self.__is_valid_color(b):
            self.__color = (r, g, b)

    def __is_valid_color(self, c1):
        if c1 < 0 or c1 > 255:
            return False
        return True

    def __is_valid_sides(self, sid):
        if isinstance(sid, int):

            return True
        else:
            return False

    def set_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for i in range(0, len(sides)):
            if not self.__is_valid_sides(i):
                return False

        for i in range(0, len(sides)):
            self.__sides[i] = sides[i]

    def set_sides_f(self, *sides):
        sids = []
        for item in sides:
            sids.append(item)

        if len(sids) == 1:  # если одна длина, то все стороны такие же

            sids = self.set_sides_1(sids[0])
        elif len(sids) != self.sides_count:
            sids = self.set_sides_1(1)

        self.__sides = sids

    def get_sides(self):
        return self.__sides

    def set_sides_1(self, dl):  # заполнение параметра
        sides = []
        for i in range(0, self.sides_count):
            sides.append(dl)
        return sides

    def get_color(self):
        return self.__color

    def __len__(self):
        '''
        Сумма длин сторон фигуры
        '''

        l1 = 0
        for i1 in self.__sides:
            l1 += i1
        return l1


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        Figure.__init__(self, color, *sides)
        dl = self.get_sides()

        self._radius = dl[0] / (2 * pi)

    def get_square(self):
        return self._radius ** 2 * pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        Figure.__init__(self, color, *sides)

    def get_square(self):
        '''
        площадь треугольника по формуле Герона
        :return:
        '''
        p = len(self) / 2
        sid = self.get_sides()
        return math.sqrt(p * (p - sid[0]) * (p - sid[1]) * (p - sid[2]))


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        '''
        объём куба
        '''
        sid = self.get_sides()
        return sid[0] ** 3


if __name__ == "__main__":
    # Код    для    проверки:
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    ###
    # круг
    print("------------")
    print("круг")
    circ1 = Circle((15, 200, 100), 5)
    print(f'"Периметр -"{len(circ1)}')
    print(f'"Площадь -"{circ1.get_square()}')

    # треугольник
    print("треугольник")
    tr1 = Triangle((15, 200, 100), 5, 3, 4)
    print(f'"Периметр -"{len(tr1)}')
    print(f'"Площадь -"{tr1.get_square()}')

    # куб
    print("куб")
    cube1 = Cube((222, 35, 130), 6)
    print(f'"Сумма длин рёбер -"{len(cube1)}')
    print(f'"Объём -"{cube1.get_volume()}')
