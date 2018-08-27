from itertools import product

def pentagonal():
    base = 0
    while True:
        base += 1
        yield int(base*((3*base)-1)/2)

penta_gen = pentagonal()
ps = set()
for _ in range(10000):
    ps.add(next(penta_gen))
print(len(ps))

matching = [x for x in product(ps, repeat=2) if x[0]-x[1] in ps and x[0]+x[1] in ps] 
print(len(matching))
print(sorted()
