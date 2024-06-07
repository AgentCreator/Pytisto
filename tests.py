import codewars_test as test
from main import tru_RPS as RPS
import time, random

tru_RPS = lambda p1, p2: "player 1 won!" if {"rock": "scissors", "scissors": "paper", "paper": "rock"}[p1] == p2 else "player 2 won!" if {"rock": "scissors", "scissors": "paper", "paper": "rock"}[p2] == p1 else "draw!"


def timee(a):
    def timing():
        start_time = time.time()
        a()
        print(time.time() - start_time, "s")
        return time.time() - start_time

    return timing

@timee
@test.describe('tests test')
def example_tests():
    @timee
    @test.it('static tests')
    def example_test_case():
        test.assert_equals(RPS("rock", "scissors"), "player 1 won!")
        test.assert_equals(RPS("rock", "rock"), "draw!")
        test.assert_equals(RPS("scissors", "rock"), "player 2 won!")
    @timee
    @test.it("haha")
    def haha():
        for _ in range(10_000):
            test.assert_equals(2 + 2, 3)
    @timee
    @test.it("random tests")
    def random_tests():
        for i in range(10_000_000):
            o = random.choice(["rock", "paper", "scissors"])
            p = random.choice(["rock", "paper", "scissors"])
            test.assert_equals(RPS(o, p), tru_RPS(o, p))