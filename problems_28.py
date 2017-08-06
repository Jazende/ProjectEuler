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

def problem_33():
    num = [x for x in range(11, 101) if not (x%10 == 0) and not str(x)[0] == str(x)[1]]
    den = [x for x in range(11, 101) if not (x%10 == 0) and not str(x)[0] == str(x)[1]]
    results = []
    reply = 1
    for x in num:
        for y in den:
            if str(x)[1] == str(y)[0]:
                if (int(str(x)[0])/int(str(y)[1])) == x/y:
                    print(x, y, x/y, (int(str(x)[0])/int(str(y)[1])))
                    results.append((int(str(x)[0]), (int(str(y)[1]))))
                    reply *= int(str(x)[0])/int(str(y)[1])
    print(reply)

problem_33()
