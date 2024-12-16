import unittest

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


class TournamentTest(unittest.TestCase):
    all_results = []

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
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({place: participant.name for place, participant in results.items()})
        self.assertEqual(results[1].name, "Усэйн")

    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({place: participant.name for place, participant in results.items()})
        self.assertEqual(results[1].name, "Андрей")

    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.append({place: participant.name for place, participant in results.items()})
        self.assertEqual(results[1].name, "Усэйн")

if __name__ == "__main__":
    unittest.main()
