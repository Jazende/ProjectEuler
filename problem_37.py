def problem_37():
    from math import sqrt
    def is_prime(getal):
        if getal == 1:
            return False
        for i in range(2, int(round(sqrt(getal)))+1 ):
            if getal % i == 0:
                return False
        return True
    def prime_sides(getal):
        if not is_prime(getal):
            return False
        for i in range(1, len(str(getal))):
            if not is_prime(int(str(getal)[i:])):
                return False
            if not is_prime(int(str(getal)[:i])):
                return False
        else:
            return True
    result =sum([x for x in range(11, 1000000, 2) if prime_sides(x)])
    print(result)
    return result
problem_37()
