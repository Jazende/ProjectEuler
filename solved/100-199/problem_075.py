# for m and n where m & n are pos int and m > n
# a = m² - n²
# b = 2nm
# c = n² + m²
# a² + b² = c²

def pythagorean_triple(m, n):
    return [m*m - n*n, 2*n*m, n*n + m*m]

def create_triples():
    m = 2
    while True:
        for n in range(1, m):
            yield pythagorean_triple(m, n)
        m += 1

        # stop when: if [@n=1] m is such that L > 1_500_000
        # L = (m² - n²) + 2nm + (n²+m²)
        # (m² - n²) + 2nm + (n² + m²) > 1_500_000
        # 2m² + 2m > 1_500_000  
        #  m² +  m >   750_000  | m(865) = 748225 | m(866) = 750822
        if m > 866: break

generator = create_triples()
lengths = {}

while True:
    try:
        next_triple = next(generator)
    except StopIteration:
        break

    counter = [0, 0, 0]
    while True:
        counter[0] += next_triple[0]
        counter[1] += next_triple[1]
        counter[2] += next_triple[2]
        l = sum(counter)
        if l > 1_500_000: break
        if not l in lengths: lengths[l] = set()
        lengths[l].add(tuple(sorted(counter)))

print(sum(1 for key, value in lengths.items() if len(value) == 1))
