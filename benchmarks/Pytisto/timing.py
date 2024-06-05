import random, time
from pytisto import *
from main import tru_RPS as RPS


def timee(a):
    def timing():
        starttime = time.time()
        a()
        print(time.time()-starttime,"s")
    return timing



tru_RPS = lambda p1, p2: "player 1 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p1] == p2 else "player 2 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p2] == p1 else "draw!"

@timee
def testies():
    tests([
        test_group("static tests", [
            assert_equals(RPS("rock", "scissors"), "player 1 won!"),
            assert_equals(RPS("rock", "rock"), "draw!"),
            assert_equals(RPS("scissors", "rock"), "player 2 won!"),
        ]),
        test_group("haha", [
            assert_equals(2+2, 3) for _ in range(10_000)
        ]),
        test_group("random tests", [
            assert_equals(RPS(i, o), tru_RPS(i,o)) for i, o in [(random.choice(["rock", "paper", "scissors"]), random.choice(["rock", "paper", "scissors"])) for _ in range(10_000_000)]
        ]),

    ])

testies()