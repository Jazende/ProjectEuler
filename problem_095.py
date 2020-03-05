import operator

def sum_divisors(number):
    sum = 1
    upper = int(number**(1/2))+2
    for i in range(2, upper):
        if number % i == 0:
            sum += i
            sum += number // i
    return sum

def day_one(max_=1_000_000):
    possible_numbers = {}
    for x in range(2, max_):
        sum_ = sum_divisors(x)
        if sum_ == 1:
            continue
        if sum_ > 999_999:
            continue
        if sum_ == x:
            continue
        possible_numbers[x] = sum_
    
    found_chains = {}

    while True:
        try:
            key, value = possible_numbers.popitem()
        except KeyError:
            break
        chain = [True, key, value]
        new_value = value
        while True:
            if not new_value in possible_numbers:
                chain[0] = False
                break
            new_value = possible_numbers.pop(new_value)
            if new_value in chain:
                found_idx = chain.index(new_value)
                chain = [True] + chain[found_idx:]
                break
            chain.append(new_value)
        if chain[0]:
            found_chains[min(chain[1:])] = len(chain)-1
        
    print(max(found_chains.items(), key=operator.itemgetter(1)))
            
day_one()
