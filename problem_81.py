import cProfile

with open('p081_matrix.txt', 'r') as f:
    raw_input = f.read()
    raw_input.strip()

matrix = {x: {} for x in range(len(raw_input.split("\n")))}

for idx_l, line in enumerate(raw_input.split("\n")):
    for idx_r, nr in enumerate(line.split(",")):
        matrix[idx_l][idx_r] = int(nr)

def euler_81():
    min_ = 0


cProfile.run('euler_81()')
