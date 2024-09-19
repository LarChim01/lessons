class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь.
        self.sound = 'Frrr'  # звук

    def run(self, dx):
        self.x_distance += dx


class Eangle:
    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eangle):
    def __init__(self):
        Horse.__init__(self)
        Eangle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


if __name__ == '__main__':
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())
    p1.voice()
