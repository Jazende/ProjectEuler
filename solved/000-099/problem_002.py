def problem_2(max_=4000000):
    """Problem 2
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    sum_ = 0
    fib = [1,2]
    value = 0
    while value < max_:
        value = fib[len(fib)-2] + fib[len(fib)-1]
        fib.append(value)
    for x in [x for x in fib if (x%2==0)]:
        sum_ += x
    print(sum_)

problem_2()
