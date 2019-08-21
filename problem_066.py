from collections import Counter
from operator import mul
from functools import reduce

def list_primes(n=100_000_000):
    sieve = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# Try: memo-ization voor get-divs als het te lang loopt
def get_divisors(number):
    divisors = []
    prime_idx = 0
    max_ = int(number**(1/2))+1
    while number > 1:
        try:
            while number % primes[prime_idx] == 0:
                number //= primes[prime_idx]
                divisors.append(primes[prime_idx])
        except IndexError:
            primes.append(number)
            print("adding", number)
            continue
        prime_idx += 1
    
    return Counter(divisors)

target = 40

primes = list_primes(100_000)
x = 2
d_values = {i: None for i in range(2, target+1) if not (int(i**(1/2))**2 == i)}
# oplossing neemt 2² - 3x1² niet mee, maar is enigste optie met 1² dus kunnen manueel toevoegen
d_values[3] = 2

while True:
    search_value = (x * x) - 1
    divs = get_divisors(search_value)

    # overzicht maken van alles per 2           vb: 4x2, 2x 3
    # permutattions van alle mogelijkheden     vb: 2**2, (2x2)**2, 3**2, 6**2, 12**2







    # for key, value in divs.items():
    #     for idx in range(2, value+1, 2):
    #         c = get_divisors(search_value)
    #         c[key] -= idx
    #         d = reduce(mul, [key**value for key, value in c.items()])
    #         if d in d_values.keys():
    #             if d_values[d] == None:
    #                 d_values[d] = x
    #             else:
    #                 d_values[d] = min(d_values[d], x)
    #             print(f'd: {d:>3}, x: {x}')


    x += 1
    # if x % 100 == 0:
    #     print(len([(key, value) for key, value in d_values.items() if value is None]))
    if all([value is not None for key, value in d_values.items()]):
        break


print(d_values)
print(max([(key, value) for key, value in d_values.items() if not value is None], key=lambda x: x[1]))










































































# target = 1000

# d_values = [nr for nr in range(2, target+1) if not int(nr**(1/2))**2 == nr]

# x_value = 1
# x_square_minus_one = x_value * x_value - 1

# def is_square(nr):
#     if not hex(int(nr))[-1] in '0149':
#         return False
#     if int(nr**(1/2))**2 == nr:
#         return True
#     return False
    

# while True:
#     if x_value % 1000 == 0:
#         print(x_value, len(d_values))
#     x_square_minus_one += 2 * x_value + 1
#     d_values = [d for d in d_values if not is_square(x_square_minus_one / d)]
    
#     if len(d_values) < 10:
#         print(d_values)
#     if len(d_values) <= 1:
#         print(d_values)
#         break
    
#     x_value += 1











# while True:
#     if x_value % 1000 == 0:
#         print(len(d_values))
#     x_square = (x_value*x_value) - 1
#     new_d_values = []
    
#     for d in d_values:
#         test_val = x_square / d
#         if not int(test_val**(1/2))**2 == test_val:
#             new_d_values.append(d)
    
#     d_values = new_d_values
    
#     if len(d_values) < 10:
#         print(d_values)
#     if len(d_values) <= 1:
#         print(d_values)
#         break
    
#     x_value += 1







# squares = [x**2 for x in range(1, 1_000_000)]

# #    X     in squares
# for square in squares:
#     print(len(D_values))
#     new_D_values = []
#     # minus_one = X-1 = Dy²
#     minus_one = square-1

#     for D in D_values:
#         #minus_one // D = Dy² // D = y²
#         if not (minus_one // D) in squares:
#             new_D_values.append(D)
    
#     D_values = new_D_values

#     if len(D_values) < 10:
#         print(D_values)
#     if len(D_values) == 1:
#         print(D_values)
#         break



# for square in squares:
#     print(len(D_values))
#     new_D_values = []

#     for D in D_values:
#         if not (D * square) + 1 in squares:
#             new_D_values.append(D)
    
#     D_values = new_D_values

#     if len(D_values) < 10:
#         print("  > ", D_values)
#     if len(D_values) == 1:
#         break

# print("---")
# print(D_values)




# max_x = 0
# for D in range(2, 1001):
#     if D in squares:
#         continue

#     found = False
#     string_ = f'x² - {D}y² = 1'
#     print(f'{string_:>20}')
#     for square in squares:
#         if (1 + (D * square)) in squares:
#             max_x = (1 + (D * square)) ** (1/2)
#             found = True
#             break
#     if not found:
#         print(f"No solution for {D}")


# print(max_x)