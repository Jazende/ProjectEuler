def problem_17():
    import re
    matches = {"\d[02-9]0": 0, "\d2\d": 6,
               "\d[02-9]1": 3, "\d3\d": 6,
               "\d[02-9]2": 3, "\d4\d": 5,
               "\d[02-9]3": 5, "\d5\d": 5,
               "\d[02-9]4": 4, "\d6\d": 5,
               "\d[02-9]5": 4, "\d7\d": 7,
               "\d[02-9]6": 3, "\d8\d": 6,
               "\d[02-9]7": 5, "\d9\d": 6,
               "\d[02-9]8": 5, "1\d\d": 13,
               "\d[02-9]9": 4, "2\d\d": 13,
               "\d10": 3, "3\d\d": 15,
               "\d11": 6, "4\d\d": 14,
               "\d12": 6, "5\d\d": 14,
               "\d13": 8, "6\d\d": 13,
               "\d14": 8, "7\d\d": 15,
               "\d15": 7, "8\d\d": 15,
               "\d16": 7, "9\d\d": 15,
               "\d17": 9, "[1-9]00": -3,
               "\d18": 8, 
               "\d19": 8}

    numbers = [str(x) for x in range(10)]
    sum_ = 0
    for x in numbers:
        for y in numbers:
            for z in numbers:
                print(x+y+z, end = " ")
                count = 0
                for match in matches:
                    if re.match(match, x+y+z):
                        count += matches[match]
                        sum_ += matches[match]
                print(count)
    sum_ += 11
    print(sum_)
    
problem_37()
