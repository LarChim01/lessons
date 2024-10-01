from threading import Thread
from time import sleep



class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.voin = 100
        self.days = 0
        print(f'{self.name} на нас напали!')

    def run(self):
        while self.voin > 0:
            self.days += 1
            sleep(1)
            self.voin -= self.power
            print(f'{self.name} сражается {self.days} {self.str_day()}, осталось {self.voin} воинов.')
        print(f'{self.name} всех победил спустя {self.days} {self.str_day()}!')

    def str_day(self):
        dey_ = int(str(self.days)[-1])
        if dey_ == 1:
            return 'день'
        elif dey_ in (2,3,4):
            return 'дня'
        else:
            return 'дней'





def str_day(days):

            dey_ = str(days)[-1]
            print(dey_)
            if dey_ == 1:
                return 'день'
            elif dey_ in (2,3,4):
                return 'дня'
            else:
                return 'дней'





if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    first_knight.start()
    second_knight = Knight("Sir Galahad", 20)
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print("Битва закончилась!")




