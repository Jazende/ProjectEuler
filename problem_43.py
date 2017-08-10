def problem_43():
    from itertools import permutations
    sum_ = 0
    for x in permutations(list("0123456789")):
        if int(x[7]+x[8]+x[9])%17==0:
            if int(x[6]+x[7]+x[8])%13==0:
                if int(x[5]+x[6]+x[7])%11==0:
                    if int(x[4]+x[5]+x[6])%7==0:
                        if int(x[5])%5==0:
                            if (int(x[2])+int(x[3])+int(x[4]))%3==0:
                                if int(x[3])%2==0:
                                    sum_ += int(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9])
    print(sum_)

import cProfile
cProfile.run('problem_43()')


