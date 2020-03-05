def problem_4(digits=3, brute_force = True):
    def is_palindrome(number):
        if str(number) == str(number)[::-1]:
            return True
        else:
            return False
    if brute_force == True:
        numbers = [x for x in range(10**(digits-1),10**digits) if len(str(x)) == digits]
        numbers = sorted(numbers, reverse=True)
        abs_max = numbers[0]**2
        curr_max = (0, 0, 0)
        for x in numbers:
            for y in numbers:
                if x * numbers[0] < curr_max[0]:
                    break
                if is_palindrome(x*y) == True:
                    if x*y > curr_max[0]:
                        curr_max = (x*y, x, y)
        print(curr_max)

problem_4()
