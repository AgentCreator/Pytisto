import unittest, random, time

from main import tru_RPS as RPS
tru_RPS = lambda p1, p2: "player 1 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p1] == p2 else "player 2 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p2] == p1 else "draw!"

def timee(a):
    def timing(b):
        starttime = time.time()
        a(b)
        print(time.time()-starttime,"s")
    return timing


class TestStringMethods(unittest.TestCase):

    @timee
    def test_upper(self):
        self.assertEqual(RPS("rock", "scissors"), "player 1 won!")
        self.assertEqual(RPS("rock", "rock"), "draw!")
        self.assertEqual(RPS("scissors", "rock"), "player 2 won!")
    @timee
    def test_isupper(self):
        for i in range(10_000_000):
            a = random.choice(["rock", "paper", "scissors"])
            b = random.choice(["rock", "paper", "scissors"])
            self.assertEqual(RPS(a, b), tru_RPS(a, b))


if __name__ == '__main__':

    unittest.main()