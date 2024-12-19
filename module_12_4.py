import logging
import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(message)s')

    def test_walk(self):
        try:
            runner = Runner("TestRunner", speed=-5)
            for _ in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, 50)
        except TypeError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            runner = Runner(12345, speed=5)
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
