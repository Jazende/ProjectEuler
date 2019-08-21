import cProfile

def list_primes(n=1_000_000):
    sieve = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)//(2*i)+1)
    return [0, 2] + [i for i in range(3,n,2) if sieve[i]]

primes = list_primes()

def prime_square_reminder(n):
    pn = primes[n]
    sq = pn**2
    sub = pn-1
    sup = pn+1
    first = 1
    second = 1
    for x in range(n):
        first = (first * sub) % sq
        second = (second * sup) % sq
    return (first + second) % sq

# cProfile.run('for i in range(1, 1000):\n    prime_square_reminder(i)')

for x in range(7035, 7040):
    print(f'n: {x}, pn: {primes[x]}, r: {prime_square_reminder(x)}')
print('- - - '*6)

x = 7037
while True:
    x += 1
    if prime_square_reminder(x) >= 10_000_000_000:
        print(f'n: {x}, pn: {primes[x]}, r: {prime_square_reminder(x)}')
        break

# ### Iets sneller voor kleinere getallen maar veel trager voor grote
# def prime_square_reminder(n):
#     pn = primes[n]
#     sum_ = (pn-1)**n + (pn+1)**n
#     rest = sum_ % (pn**2)
#     return rest
