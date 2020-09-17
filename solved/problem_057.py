from fractions import Fraction
import cProfile
import math

def problem_57(target):
    question_count = 0
    count = 0
    value = Fraction(1, 2)
    while True:
        value = 1/(2 + value)
        test_value = 1 + value
        num_digits = int(math.log10(test_value.numerator))+ 1
        den_digits = int(math.log10(test_value.denominator))+ 1
        if num_digits > den_digits:
            question_count += 1
        count += 1
        if count == target:
            break
    return question_count

cProfile.run('problem_57(1000)')
print(problem_57(1000))
