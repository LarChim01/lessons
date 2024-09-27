#Дополнительное практическое задание по модулю: "Наследование классов."
import math

PI = math.pi  # число пи


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        color = list(color)
        self.__color = [*color] if self.__is_valid_color(*color) else [0, 0, 0]
        if  len(sides)== 1 :
            self.__sides = list(sides * self.sides_count)
        else:
            self.__sides = list([*sides] if len(sides) == self.sides_count else [1] * self.sides_count)

    def set_color(self, *color):
        self.__color = [*color] if self.__is_valid_color(*color)  else self.__color

    def __is_valid_color(self, *color):
        for c1 in color:
            if not isinstance(c1,int) or c1 >255 or c1< 0:
                return False

        return True

    def __is_valid_sides(self, *sides):
        for sid in sides:
            if not isinstance(sid, int):
                return False

        return True

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list([*sides] if len(sides) == self.sides_count else self.__sides)




    def get_sides(self):
        return self.__sides



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
        self.__radius = self.get_sides()[0] / (2 * PI)

    def get_square(self):
        return self.__radius ** 2 * PI


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

        return self.get_sides()[0] ** 3
class Sixter(Figure):
    sides_count = 6


if __name__ == "__main__":
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
