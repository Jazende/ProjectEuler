from itertools import combinations

''' 2960 function calls in 0.001 seconds '''
with open(r'p102_triangles.txt', 'r') as f:
    print(sum([any([x > 0 for x in [combo[0][1]-((combo[0][1]-combo[1][1])*combo[0][0])/(combo[0][0]-combo[1][0]) for combo in combinations([(triangle[0], triangle[1]), (triangle[2], triangle[3]), (triangle[4], triangle[5])], r=2) if not (combo[0][0] - combo[1][0] == 0 or not (combo[0][0] < 0 < combo[1][0] or combo[0][0] > 0 > combo[1][0]))]]) and any ([x < 0 for x in [combo[0][1]-((combo[0][1]-combo[1][1])*combo[0][0])/(combo[0][0]-combo[1][0]) for combo in combinations([(triangle[0], triangle[1]), (triangle[2], triangle[3]), (triangle[4], triangle[5])], r=2) if not (combo[0][0] - combo[1][0] == 0 or not (combo[0][0] < 0 < combo[1][0] or combo[0][0] > 0 > combo[1][0]))]]) for triangle in [[int(y) for y in line.split(',')] for line in f.read().strip().split('\n')]]))

''' 3961 function calls in 0.003 seconds '''
def pos_and_neg(iterable):
    return True if any([x > 0 for x in iterable]) and any([x < 0 for x in iterable]) else False

with open(r'p102_triangles.txt', 'r') as f:
    print(sum([pos_and_neg([combo[0][1] - ((combo[0][1] - combo[1][1]) * combo[0][0]) / (combo[0][0] - combo[1][0]) for combo in combinations([(triangle[0], triangle[1]), (triangle[2], triangle[3]), (triangle[4], triangle[5])], r=2) if not (combo[0][0] - combo[1][0] == 0 or not (combo[0][0] < 0 < combo[1][0] or combo[0][0] > 0 > combo[1][0]))]) for triangle in [[int(y) for y in line.split(',')] for line in f.read().strip().split('\n')]]))



# with open(r'p102_triangles.txt', 'r') as f:
#     triangles = [[int(y) for y in line.split(',')] for line in f.read().strip().split('\n')]

# def valid_x_values(combo):
#     return False if combo[0][0] - combo[1][0] == 0 or not (combo[0][0] < 0 < combo[1][0] or combo[0][0] > 0 > combo[1][0]) else True

# def get_b_values(combo):
#     return combo[0][1] - ((combo[0][1] - combo[1][1]) * combo[0][0]) / (combo[0][0] - combo[1][0])

# def pos_and_neg(iterable):
#     return True if any([x > 0 for x in iterable]) and any([x < 0 for x in iterable]) else False

# def create_sets(numbers):
#     return [(numbers[0], numbers[1]), (numbers[2], numbers[3]), (numbers[4], numbers[5])]

# print(sum([pos_and_neg([get_b_values(combo) for combo in combinations(create_sets(triangle), r=2) if valid_x_values(combo)]) for triangle in triangles]))
