def solution(N, stages):
    stageset = list(range(1,N+1))
    print(stageset)
    failper = []
    answer = []
    lst = []
    for stage in range(1,max(stages)):
        failper.append(stages.count(stage)/len(stages))
        print(stage)
        print(stages.count(stage))
        print(len(stages))
        while stage in stages:
            stages.remove(stage)
    print(failper)
    for i in range(len(stageset)):
        lst.append([failper[i],stageset[i]])
    lst = sorted(lst)
        
        
solution(5,[2,1,2,6,2,4,3,3])
