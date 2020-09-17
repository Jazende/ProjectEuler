def problem_16(target=1000):
    number = 2**target
    result = 0
    for i in str(number):
        result+= int(i)
    return result


problem_16()
