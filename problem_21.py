def problem_21(target=10000):
    def divisors(getal):
        divisors = []
        for x in range(1,getal+1):
            if getal%x == 0:
                if x in divisors:
                    break
                elif x**2 == getal:
                    divisors.append(x)
                else:
                    divisors.append(x)
                    divisors.append(int(getal/x))
        if getal in divisors:
            divisors.remove(getal)
        return divisors
    def amic(getal):
        if sum(divisors(sum(divisors(getal)))) == getal:
            if sum(divisors(getal)) == getal:
                return 0
            else:
                return getal
        else:
            return 0
    return sum([amic(x) for x in range(1, target+1)])


problem_21()
