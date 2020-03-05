def problem_48(target=1000):
    """The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000."""
    # som van elke keer: laatste digit pow getal
    number = str(sum([((x%(10**10))**x)%(10**10) for x in range(1, target+1)]))
    return number[len(number)-10:]
problem_48()
