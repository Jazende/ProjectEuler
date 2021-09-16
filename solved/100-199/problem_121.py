from itertools import product
import cProfile

turns = 15

def run(turns):
    perm = product([0, 1], repeat=turns)
    chances = [[x / (x+1) for x in range(1, turns+2)], [1/(x+1) for x in range(1, turns+2)]]
    win_chances = 0
    loss_chances = 0
    for permutation in perm:
        chance = 1
        out_of = 1
        for idx, nr in enumerate(permutation):
            chance *= chances[nr][idx]
            out_of *= idx+2
        # print(chance, chance*out_of, out_of)
        if sum(permutation) <= len(permutation)//2:
            loss_chances += chance*out_of
        else:
            win_chances += chance*out_of

    total_chances = win_chances+loss_chances
    win_percentage = win_chances / (total_chances)
    # print(int(1/win_percentage))
    return int(1/win_percentage)

print(run(15))