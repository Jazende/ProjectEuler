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
