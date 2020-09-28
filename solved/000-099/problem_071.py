def problem_71(target= 1000000):
    from itertools import product
    cur_closest = 0
    info_closest = (0, 1)
    target_value = 3/7
    count =0
    for j in range(1, target+1):
        min_bound = int(round((j*info_closest[0])/info_closest[1]))-1
        max_bound = int(round(((j*3))/7))+1
        for i in range(min_bound, max_bound):
            count += 1
            if cur_closest < i/j < target_value:
                cur_closest = i/j
                info_closest=(i, j)
    print(count)

    for i in range(2, int(round(info_closest[0]+1/2))+1):
        while (info_closest[0]%i==0) and (info_closest[1]%i==0):
            info_closest = (int(info_closest[0]/i), int(info_closest[1]/i))
    return (cur_closest, info_closest)

problem_71()
