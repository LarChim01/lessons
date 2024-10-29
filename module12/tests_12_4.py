import rt_with_exceptions as runner
import unittest
import logging
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format="%(asctime)s) | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:

            r1 = runner.Runner(7, 4)

            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                r1.walk()

            self.assertEqual(r1.distance, 50)
        except Exception as exc:
            logging.error('Ошибка - "test_walk"', exc_info=True)

    def test1_walk(self):
        try:
            r1 = runner.Runner("Ходок", 5)

            for i in range(10):
                r1.walk()

            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk1" выполнен успешно')
        except Exception as exc:
            logging.error('Ошибка - "test1_walk"', exc_info=True)

    def test2_walk(self):
        try:
            r1 = runner.Runner("Ходок", -8)
            print('re')

            for i in range(10):
                r1.walk()

            self.assertEqual(r1.distance, 50)
            logging.info('"test2_walk" выполнен успешно')
        except Exception as exc:
            logging.error('Ошибка-"test2_walk"', exc_info=True)

    def test_run(self):
        try:
            r2 = runner.Runner("Бегун", 5)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except Exception as exc:
            logging.error('Ошибка - "test_run"', exc_info=True)

    def test_challenge(self):
        try:
            r1 = runner.Runner("Ходок", 5)
            r2 = runner.Runner("Бегун", 5)
            for i in range(10):
                r1.walk()

            for i in range(10):
                r2.run()

            self.assertNotEqual(r1.distance, r2.distance)
            logging.info('"test_challenge" выполнен успешно')

        except Exception as exc:
            logging.error('Ошибка - test_challenge', exc_info=True)


if __name__ == "__main__":
    unittest.main()
