class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


if __name__ == '__main__':
    r1 = Runner("Z")
    for i in range(10):
        r1.walk()

    print(r1.distance)