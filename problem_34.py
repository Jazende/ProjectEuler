def problem_34(target=10000000):
    from collections import Counter
    answer_1 = 0
    answer_89 = 0
    up_to_100 = []
    next_in_chain = lambda x: sum([int(x)**2 for x in str(x)])
    for x in range(1, 1000):
        while x not in [1, 89]:
            x = next_in_chain(x)
        up_to_100.append(x)
    for x in range(1, target):
        if up_to_100[next_in_chain(x)] == 1:
            answer_1 += 1
        else:
            answer_89 += 1
        
    return (answer_1, answer_89)

problem_34()
