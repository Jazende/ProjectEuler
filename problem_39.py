def problem_39(target=1000):
    from math import sqrt
    from collections import Counter
    answers = {}
    def check(results):
        answer = []
        for a in range(1, results):
            for b in range(a, results+1):
                c = sqrt(a**2 + b**2)
                if a+b+c == results:
                    answer.append((a, b, int(c), int(a)+int(b)+int(c)))
                if a+b+c > results:
                    break
        return answer
    for x in range(1, target+1):
        try:
            j = check(x)
            for i in j: 
                a = i[0]
                b = i[1]
                c = i[2]
                d = i[3]
                if d in answers.keys():
                    answers[d] = answers[d] + [(a, b, c)]
                else:
                    answers[d] = [(a, b, c)]
        except:
            pass
    print(answers)
    return answers

a = problem_39()
