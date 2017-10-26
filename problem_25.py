def problem_25(target_dig = 1000):
    a = 1
    b = 1
    c = 0
    count = 2
    while len(str(b)) < target_dig:
        a = b + a
        c = b
        b = a
        a = c
        count+= 1
    print(count)
