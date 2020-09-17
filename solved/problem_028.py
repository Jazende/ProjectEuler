def problem_28(target=1001):
    start = 1
    for x in range(2, target+1):
        if x%2 == 1:
            start += x**2
            start += x**2 - (x-1)
            start += x**2 - (x-1)*2
            start += x**2 - (x-1)*3
            print("x: ", x, "\t\t", x**2, x**2 - (x-1), x**2 - (x-1)*2, x**2 - (x-1)*3)
    print(start)
    return start
