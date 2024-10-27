#Домашнее задание по теме "Методы Юнит-тестирования"
"""
Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

TournamentTest - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:

    Бегун по имени Усэйн, со скоростью 10.
    Бегун по имени Андрей, со скоростью 9.
    Бегун по имени Ник, со скоростью 3.

tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):

    Усэйн и Ник
    Андрей и Ник
    Усэйн, Андрей и Ник.

Как можно понять: Ник всегда должен быть последним.
"""

import runner_and_tournament as runner

import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results={}


    def setUp(self):
        self.b = runner.Runner('Усэйн', 10)
        self.b1 = runner.Runner('Андрей', 9)
        self.b2 = runner.Runner('Ник', 3)

    def test_start(self):
        t1 = runner.Tournament(90, self.b,  self.b2)
        t2 = runner.Tournament(90, self.b1, self.b2)
        t3 = runner.Tournament(90, self.b,self.b1, self.b2)
        i = 0
        for item in (t1, t2, t3):
            i += 1

            self.all_results[i] = item.start()


    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(f'Забег №{i}')
            for key, value in cls.all_results[i].items():
                print(f'{key} : {value}')




if __name__ == '__main__':
    unittest.main()
