def problem_67():
    import re
    lines = []
    with open('p067_triangle.txt', 'r') as f:
        for line in f:
            temp = re.findall("\d{1,2}", line)
            lines.append([int(x) for x in temp])

    curr_line = len(lines)-2
    while curr_line >= 0:
        for idx, number in enumerate(lines[curr_line]):
            lines[curr_line][idx] = number + max(lines[curr_line+1][idx],
                                                 lines[curr_line+1][idx+1])
        curr_line -= 1
    print(lines[0])
    
problem_67()
