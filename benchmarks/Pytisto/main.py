def tru_RPS(p1, p2):
    return "player 1 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p1] == p2 else "player 2 won!" if {"rock":"scissors", "scissors":"paper", "paper":"rock"}[p2] == p1 else "draw!"
