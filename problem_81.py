import copy
import cProfile

def laad_dict():
    with open('p081_matrix.txt', 'r') as f:
        raw_input = f.read()
        raw_input.strip()

    matrix = {x: {} for x in range(len(raw_input.split("\n")))}

    for idx_l, line in enumerate(raw_input.split("\n")):
        for idx_r, nr in enumerate(line.split(",")):
            matrix[idx_l][idx_r] = int(nr)

    return matrix

def get_triangle(matrix):
    len_mat = len(matrix)
    full_triangle = []

    for idx in range(0, len_mat):
        counter = 0
        row = []
        for j in range(0, idx+1):
            row.append(matrix[idx-counter][counter])
            counter += 1
        full_triangle.append(row)

    for idx in range(1, len(matrix)):
        counter = len_mat-1
        row = []
        for j in range(0, counter+1-idx):
            row.append(matrix[counter-j][j+idx])
        full_triangle.append(row)

    return full_triangle

matrix = laad_dict()
full_triangle = get_triangle(matrix)

def euler_81(input_):
    lines = copy.copy(input_)
    curr_line = 1
    base_value = lines[0][0]
    while curr_line < len(lines):
        if len(lines[curr_line]) > len(lines[curr_line-1]):
            for idx, number in enumerate(lines[curr_line]):
                if idx == 0:
                    lines[curr_line][idx] += lines[curr_line - 1][0]
                elif idx == len(lines[curr_line])-1:
                    lines[curr_line][idx] += lines[curr_line - 1][idx-1]
                else:
                    lines[curr_line][idx] += min(lines[curr_line-1][idx-1],
                                                 lines[curr_line-1][idx])


        else:
            for idx, number in enumerate(lines[curr_line]):
                lines[curr_line][idx] += min(lines[curr_line-1][idx+1],
                                             lines[curr_line-1][idx])         
        curr_line += 1
    return lines[len(lines)-1]

print(euler_81(full_triangle))
cProfile.run('euler_81(full_triangle)')
