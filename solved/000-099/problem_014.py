def problem_14(target=1000000):
    def collatz_chain(input_):
        count = 0
        while input_ > 1:
            count += 1
            if input_%2==0:
                input_ /= 2
            else:
                input_ = input_*3+1
        return count
    max_collatz = 0
    for i in range(1, target):
        col = collatz_chain(i)
        if col > max_collatz:
            max_collatz = col
            print(i, col)

problem_14()
