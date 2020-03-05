def problem_9(target=1000):
    """ A Pythagorean triplet is a set of three natural numbers,
    a < b < c, for which, a2 + b2 = c2

    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""

    for i in range(1, target-2):
        for j in range(i, target-1):
            if i**2 + j**2 == (target-i-j)**2:
                print(i, j, (target-i-j))
                print(i*j*(target-i-j))

problem_9()
