import unittest
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
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = Runner('Dyon')
        i = 0
        while i < 10:
            i += 1
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)
    def test_run(self):
        runner_2 = Runner('Kate')
        j = 0
        while j < 10:
            j += 1
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)
    def test_challenge(self):
        runner_3 = Runner('Leon')
        runner_4 = Runner('Michel')
        k = 0
        while k < 10:
            k += 1
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)