##Take the number 192 and multiply it by each of 1, 2, and 3:
##
##192 × 1 = 192
##192 × 2 = 384
##192 × 3 = 576
##
##By concatenating each product we get the 1 to 9 pandigital, 192384576. 
##We will call 192384576 the concatenated product of 192 and (1,2,3)
##
##The same can be achieved by starting with 9 and multiplying by
##1, 2, 3, 4, and 5, giving the pandigital, 918273645,
##which is the concatenated product of 9 and (1,2,3,4,5).
##
##What is the largest 1 to 9 pandigital 9-digit number that can be
##formed as the concatenated product of an integer with (1,2, ... , n)
##where n > 1?

check_set = [x for x in range(1, 10)]

def concat(number):
    result = ""
    count = 1
    while True:
        result += str(number*count)
        count += 1
        if len(result) > 9:
            return False
        if len(result) == 9 == len(set([int(x) for x in result])) and count > 1:
            if sorted([int(x) for x in list(result)]) == sorted(check_set):
                return int(result)

def problem_38():
    cur_max = 0
    cur_value = 0
    for x in range(1, 99999):
        if x % 1000000 == 0:
            print(x)
        value = concat(x)
        if not value is False:
            if value > cur_max:
                cur_max = value
                cur_value = x
                print(cur_value, cur_max)
    return (cur_value, cur_max)

problem_38()
                   
