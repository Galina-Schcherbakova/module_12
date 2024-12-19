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
    is_frozen = False

    def test_walk(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[len(finishers) + 1] = participant
                    self.participants.remove(participant)
                    break
        return finishers

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class TournamentTest(unittest.TestCase):
    all_results = []
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)
            print()

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    def test_race_1(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({place: participant.name for place, participant in results.items()})
        self.assertEqual(results[1].name, "Усэйн")

    def test_race_2(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({place: participant.name for place, participant in results.items()})
        self.assertEqual(results[1].name, "Андрей")

    def test_race_3(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({place: participant.name for place, participant in results.items()})
        self.assertEqual(results[1].name, "Усэйн")
