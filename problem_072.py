import cProfile

def problem_072(n):
    phi = list(range(n+1))
    print("b", phi)
    for i in range(2, n+1):
        if phi[i] == i:
            for j in range(i, n+1, i):
                print(f"{j}: {phi[j]} => {phi[j] // i * (i-1)} ({phi[j] // i} * {i - 1})")
                phi[j] = phi[j] // i * (i-1)
        print(i, phi)
    return sum(phi)-1

print(problem_072(30))