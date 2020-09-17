''' The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

from collections import Counter

''' 192587 function calls (192579 primitive calls) in 3.028 seconds '''
cubes = []
idx = 1
    
while True:
    cubes.append((idx, Counter(i for i in str(idx**3))))
    perm_cubes = [other for other in cubes if other[1] == cubes[-1][1]]
    if len(perm_cubes) == 5:
        print(min(perm_cubes, key=lambda x: x[0]**3)[0]**3)
        break
    idx += 1
