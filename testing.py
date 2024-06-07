import random

import time


def tru_rps(p1, p2):
    return "player 1 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p1] == p2 else "player 2 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p2] == p1 else "draw!"


def timee(a):
    def timing():
        starttime = time.time()
        a()
        print(f"{time.time()-starttime} s")
    return timing


@timee
def testicle():
    expr_tests(RPS, [
        {
            (vals := (choice(["rock", "paper", "scissors"]), choice(["rock", "paper", "scissors"]))): tru_rps(*vals) for
            _ in range(10_000_000)
        }
    ])

if __name__ == '__main__':
    testicle()
