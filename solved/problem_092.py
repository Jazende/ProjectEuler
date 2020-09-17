import cProfile

##def prob_92():
##    nrs = {x: None for x in range(1, 10000001)}
##    print("starting")
##    nrs[1] = 1
##    nrs[89] = 89
##
##    def end_of_chain(nr):
##        if not nrs[nr] is None:
##            return nrs[nr]
##        else:
##            getal = sum([int(x)**2 for x in str(nr)])
##            new_nr = end_of_chain(getal)
##            nrs[nr] = new_nr
##            return new_nr
##
##    for number in nrs:
##        if not nrs[number]:
##            end_of_chain(number)
##
##    count_89 = 0
##    count_1 = 0
##    count_none = 0
##
##    for number, value in nrs.items():
##        if value == 89:
##            count_89 += 1
##        if value == 1:
##            count_1 += 1
##        if value == None:
##            count_none+= 1
##    print(count_89, count_1, count_none)


##def prob_92():
##    ## 58 sec
##    nrs = {x: None for x in [1, 89]}
##    def end_of_chain(nr):
##        if nr in nrs:
##            return nrs[nr]
##        else:
##            getal = sum([int(x)**2 for x in str(nr)])
##            new_nr = end_of_chain(getal)
##            nrs[nr] = new_nr
##            return new_nr
##    count = 0
##    for i in range(1, 10000001):
##        if end_of_chain(i) == 89:
##            count+=1
##    print(count)

def prob_92():
    nrs = {}
    nrs[tuple(sorted([int(x) for x in str(1) if not x == "0"]))] = 1
    nrs[tuple(sorted([int(x) for x in str(89) if not x == "0"]))] = 1
    def end_of_chain(nr):
        set_ = tuple(sorted([int(x) for x in str(nr) if not x == "0"]))
        if set_ in nrs:
            return nrs[set_]
        else:
            getal = sum([int(x)**2 for x in str(nr)])
            new_nr = end_of_chain(getal)
            nrs[set_] = new_nr
            return new_nr
    count = 0
    for i in range(1, 10000001):
        if end_of_chain(i) == 89:
            count+=1
    print(count)

    
cProfile.run('prob_92()')
