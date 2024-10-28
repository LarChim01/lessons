#Домашнее задание по теме "Простые Юнит-Тесты"
#    test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
#    Далее вызовите метод walk у этого объекта 10 раз.
#    После чего методом assertEqual сравните distance этого объекта со значением 50.
#     test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
#     Далее вызовите метод run у этого объекта 10 раз.
#     После чего методом assertEqual сравните distance этого объекта со значением 100.
#     test_challenge - метод в котором создаются 2 объекта класса Runner с
#     произвольными именами.
#     Далее 10 раз у объектов вызываются методы run и walk соответственно.
#     Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
# чтобы убедится в неравенстве результатов.
import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r1 = runner.Runner("Ходок")
        for i in range(10):
            r1.walk()

        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_run(self):
        r2 = runner.Runner("Бегун")
        for i in range(10):
            r2.run()

        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r1 = runner.Runner("Ходок")
        r2 = runner.Runner("Бегун")
        for i in range(10):
            r1.walk()

        for i in range(10):
            r2.run()

        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == "__main__":
    unittest.main()
