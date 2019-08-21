import time
import datetime
check = set('123456789')

def both(precision=12):
    n = 0

    first_value_n_minus_one = 0
    first_value_n = 1

    last_value_n_minus_one = 0
    last_value_n = 1
    while True:
        n += 1

        first_value_n_minus_one, first_value_n = first_value_n, first_value_n_minus_one + first_value_n
        last_value_n_minus_one, last_value_n = last_value_n, last_value_n_minus_one + last_value_n

        last_value_n_minus_one = last_value_n_minus_one % 1_000_000_000
        last_value_n = last_value_n % 1_000_000_000

        if set(str(last_value_n)) == check and check == set(str(first_value_n)[:9]):
            return n + 1
    
        if first_value_n > 10**precision and first_value_n_minus_one > 10**precision:
            first_value_n_minus_one = (first_value_n_minus_one + 5) // 10
            first_value_n = (first_value_n + 5) // 10

start = datetime.datetime.now()

for prec in range(12, 15):
    print(both(prec))

print(datetime.datetime.now() - start)