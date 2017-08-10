def problem_42():
    import re
    count = 0
    with open('p042_words.txt', 'r') as f:
        for name in re.findall("\"(\w*?)\"", f.readline()):
            if sum([list("ABCDEFGHIJKLMNOPQRSTUVWXYZ").index(y.upper())+1 for y in name]) in [(x/2)*(x+1) for x in range(100)]:
                count += 1
    print(count)
problem_42()
