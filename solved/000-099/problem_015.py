def problem_15(target=20):
    for x in range(2, 21):
        print(x, factorial(2*x)/(factorial(x)**2))

problem_15()
