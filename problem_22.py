def problem_22():
    import re
    with open("p022_names.txt", 'r') as f: print(sum([(idx+1) * sub for idx, sub in enumerate([sum([ord(x)-64 for x in name]) for name in sorted(re.findall("\"(\w*?)\"", f.readline()))])]))


problem_22()
