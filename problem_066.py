from sympy.solvers.diophantine import diop_DN

squares = [i**2 for i in range(int(100**(1/2))+1)]
min_x = []

for i in range(2, 1001):
    if i in squares:
        continue
    min_x.append([i, *diop_DN(i, 1)])

print(max(min_x, key=lambda x: x[1]))
