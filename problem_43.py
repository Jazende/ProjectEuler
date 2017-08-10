def problem_43_2():
    #0.027s
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_ = 0
    for nr_1 in numbers:
        pool_1 = numbers + []
        pool_1.remove(nr_1)
        for nr_2 in pool_1:
            pool_2 = pool_1 + []
            pool_2.remove(nr_2)
            for nr_3 in pool_2:
                pool_3 = pool_2 + []
                pool_3.remove(nr_3)
                for nr_4 in pool_3:
                    if nr_4%2 == 0:
                        pool_4 = pool_3 + []
                        pool_4.remove(nr_4)
                        for nr_5 in pool_4:
                            if (nr_3 + nr_4 + nr_5 ) % 3 == 0:
                                pool_5 = pool_4 + []
                                pool_5.remove(nr_5)
                                for nr_6 in pool_5:
                                    if nr_6%5==0:
                                        pool_6 = pool_5 + []
                                        pool_6.remove(nr_6)
                                        for nr_7 in pool_6:
                                            if (nr_5*100 + nr_6*10 + nr_7) % 7 == 0:
                                                pool_7 = pool_6 + []
                                                pool_7.remove(nr_7)
                                                for nr_8 in pool_7:
                                                    if (nr_6*100 + nr_7*10 + nr_8) % 11 == 0:
                                                        pool_8 = pool_7 + []
                                                        pool_8.remove(nr_8)
                                                        for nr_9 in pool_8:
                                                            if (nr_7*100 + nr_8*10 + nr_9) % 13 == 0:
                                                                pool_9 = pool_8 + []
                                                                pool_9.remove(nr_9)
                                                                for nr_10 in pool_9:
                                                                    if (nr_8*100 + nr_9*10 + nr_10) % 17 == 0:
                                                                        sum_ += int(str(nr_1)+str(nr_2)+str(nr_3)+str(nr_4)+str(nr_5)+\
                                                                                    str(nr_6)+str(nr_7)+str(nr_8)+str(nr_9)+str(nr_10))           
    print(sum_)

def problem_43():
    #2.3sec; 22sec als alles onderelkaar + testcounter, 15sec als alles nested in volgorde, 2,3 sec als nested in meest specifying vs minst
    from itertools import permutations
    sum_ = 0
    for x in permutations("0123456789"):
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
cProfile.run('problem_43_2()')


