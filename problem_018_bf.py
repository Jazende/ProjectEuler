def problem_18():
    import re
    input_ = """75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    input_two = """3
    7 4
    2 4 6
    8 5 9 3
    """

    lines = []
    a = re.findall("(.*?)\n", input_)
    for x in a:
        b = re.findall("\d{1,2}", x)
        lines.append(b)

    def opties_boven(row, column):
        if row == 1:
            return [[(0, 0)], [(0, 0)]]
        left = [(row-1, max(0, column-1))]
        right = [(row-1, min(len(lines[row-1])-1, column))]
        return left, right

    def add_opties(current_chain):
        laatste = current_chain[len(current_chain)-1]
        links, rechts = opties_boven(laatste[0], laatste[1])
        chain_1 = current_chain + links
        chain_2 = current_chain + rechts
        if chain_1 == chain_2:
            return [chain_1]
        return [chain_1, chain_2]

    chains = []
    too_check = []
    for idx, number in enumerate(lines[len(lines)-1]):
        chain_ = [(len(lines)-1, idx)]
        chains.append(chain_)

    for chain in chains:
        if len(chain) < len(lines):
            replies = add_opties(chain)
            for x in replies:
                chains.append(x)
        if len(chain) == len(lines):
            too_check.append(chain)

    max_ = 0
    for x in too_check:
        temp = 0
        for y in x:
            temp += int(lines[y[0]][y[1]])
        max_ = max(max_, temp)
    print(max_)

problem_18()
