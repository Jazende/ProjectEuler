from itertools import product
import cProfile

def problem_205():
    nine = [1, 2, 3, 4]
    six = [1, 2, 3, 4, 5, 6]

    nine_combs = product(nine, repeat=9)
    six_combs = product(six, repeat=6)

    nine_results = {x: {'count': 0} for x in range(min(nine)*9, max(nine)*9+1)}
    six_results = {x: {'count': 0} for x in range(min(six)*6, max(six)*6+1)}

    for results, combs in [(nine_results, nine_combs), (six_results, six_combs)]:
        while True:
            try:
                val = sum(next(combs))
            except StopIteration:
                break
            results[val]['count'] += 1

    for result in nine_results:
        for assert_value in six_results:
            variable = None
            if result > assert_value:
                variable = True
            elif result < assert_value:
                variable = False
            nine_results
    print(nine_results[9])
    return 

print(problem_205())
