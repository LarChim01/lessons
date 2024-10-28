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
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results={}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.b = runner.Runner('Усэйн', 10)
        self.b1 = runner.Runner('Андрей', 9)
        self.b2 = runner.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_start(self):
        t1 = runner.Tournament(90, self.b,  self.b2)
        t2 = runner.Tournament(90, self.b1, self.b2)
        t3 = runner.Tournament(90, self.b, self.b1, self.b2)
        t4 = runner.Tournament(90, self.b2, self.b1, self.b)
        i = 0
        for item in (t1, t2, t3):
            i += 1
            min_ = min(item.participants, key=lambda obj: (obj.speed,)).name
            max_ = max(item.participants, key=lambda obj: (obj.speed,)).name
            result = item.start()
            max_p = result[max(list(result.keys()))].name
            min_p = result[max(list(result.keys()))].name
            self.last_run(min_ , max_p)
            self.all_results[i] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def last_run(self, min_, last):
        ''' проверка, что бегун с наименьшей скоростью придёт последним'''
        self.assertEqual(min_, last)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def first_run(self, max_, first):
        ''' проверка, что бегун с самой большой скоростью придёт первым'''

        self.assertEqual(max_, first)




    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(f'Забег №{i}')
            for key, value in cls.all_results[i].items():
                print(f'{key} : {value}')




if __name__ == '__main__':
    unittest.main()

