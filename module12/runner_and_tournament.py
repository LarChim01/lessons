class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)



    def start(self):
        finishers = {}

        self.participants.sort(reverse=True, key=lambda obj: (obj.speed, ))
        place = 1
        while self.participants:

            for participant in self.participants:

                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

if __name__ == "__main__":
    b=Runner('Усэйн',10)
    b1 = Runner('Андрей', 9)
    b2 = Runner('Ник',3)
    t1 = Tournament(90, b,b2)
    t2 = Tournament(90, b1,  b2)
    t3 = Tournament(90,  b, b1, b2)
    result={}

    #
    # result[3] = t3.start()
    # result[2] = t2.start()
    # result[1] = t1.start()



    i = 0
    for item in (t1,t2,t3):
        i += 1
        item

        result[i] = item.start()

    for i in result:
        print(f'Забег № {i}')

        for key, value in result[i].items():
            print(f'{key} : {value}')




    # for key, value in result.values():
    #     print(f"{key}: {value} : {type(value)}")
    '''
      Бегун по имени Усэйн, со скоростью 10.
     Бегун по имени Андрей, со скоростью 9.
     Бегун по имени Ник, со скоростью 3.'''