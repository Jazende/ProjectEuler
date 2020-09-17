from itertools import count
import cProfile

def permuted_multiple(number, aantal=6):
    digit_set = set([int(x) for x in str(number)])
    for i in range(2, aantal+1):
        if not digit_set == set([int(x) for x in str(number*i)]):
            return False
    return True

def problem_52():
    count = 1
    while True:
        if permuted_multiple(count, 6):
            break
        count += 1
    return count

print(problem_52())
