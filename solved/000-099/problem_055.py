import cProfile

### Base functions to check validity of calculations

def check_palindromic(number):
    rev_number = int("".join([x for x in str(number)[::-1]]))
    if number == rev_number:
        return True
    else:
        return False

def lychrel(number, print_=False, count=None, ):
    if count == 50:
        if print_:
            print("Never palindromic -> Lychrel")
        return True
    if not count:
        if print_:
            print(f"Checking {number}... ", end="")
        count = 0
    rev_number = int("".join([x for x in str(number)[::-1]]))
    new_number = number+rev_number
    if check_palindromic(new_number):
        if print_:
            print(f"Palindromic after {count} cycles.")
        return False
    else:
        return lychrel(new_number, print_, count=count+1)

lychrel(47)
lychrel(349)
lychrel(4994)

### Functions om alle te checken voor comparison in cProfile
### 265897 function calls (231375 primitive calls) in 0.246 seconds

def problem_055(target=10000):
    count = 0
    for x in range(target+1):
        if lychrel(x):
            count += 1
    print(count)

problem_055()
cProfile.run('problem_055()')

### Functions met dictionary voor efficiency
