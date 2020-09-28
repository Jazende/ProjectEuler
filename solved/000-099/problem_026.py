import math

def go_until_repeat_remainder(nom, den, cur_max=1000):
    remainders = []
    cycles = 0
    while True:
        if nom < den:
            nom*=10
            cycles += 1
        if nom == den:
            break
        if nom > den:
            remainder = nom%den
            if remainder in remainders:
                cycles += 1
                break
            remainders.append(remainder)
            nom*=10
            cycles += 1
    return cycles

def problem_026(max_=1000):
    cur_max = 0
    cur_value = 0
    for x in range(2, 1000)[::-1]:
        new_value = go_until_repeat_remainder(1, x, cur_max)
        if new_value > cur_max:
            cur_max = new_value
            cur_value = x
    return cur_value

print(problem_026(1000))

def long_division(nom, den, max_count=100000000):
    result = "0."
    nom *= 10
    count = 0
    while True:
        if find_recurring(result):
            temp = float(result)
            if den*0.9 < int(1 / temp) < den *1.1:
                break
        if nom % den == 0:
            result += str(nom//den)
            break
        elif nom > den:
            result += str(nom//den)
            nom = nom%den
            nom *= 10
            continue
        elif nom < den:
            result += "0"
            nom *= 10
            continue
        count += 1
        if count == max_count:
            break
    return result

def find_recurring(text):
    rev_text = text[::-1]
    for i in range(1, len(text)//2+1)[::-1]:
        if rev_text[:i] == rev_text[i:i*2] == rev_text[i*2:i*3] == rev_text[i*3:i*4] and not int(rev_text[:i]) == 0:
            return True
    return False

def get_recurring(text):
    rev_text = text[::-1]
    for i in range(1, len(text)//2+1)[::-1]:
        if rev_text[:i] == rev_text[i:i*2] == rev_text[i*2:i*3] == rev_text[i*3:i*4] and not int(rev_text[:i]) == 0:
            return rev_text[:i]
        
def get_recurring_length(nom, den):
    division = long_division(nom, den)
    if find_recurring(division):
        return len(get_recurring(division))
    else:
        return 0

def problem_26(target):
    # fractions = {x: get_recurring_length(1, x) for x in range(2, target+1)}
    fractions = []
    for x in range(2, target+1):
        fractions.append([x, get_recurring_length(1, x)])
    fractions = sorted(fractions, key=lambda x: x[1], reverse=True)
    print(fractions[:10])
    return fractions[0]

problem_26(1000)
#print(long_division(1, 261))
