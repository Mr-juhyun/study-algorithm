def solution(n, times):
    minT = 0
    maxT = 10**20
    while maxT>minT:
        midT = (maxT+minT)//2
        complete = 0
        for t in times:
            complete += midT//t
        if complete >= n:
            maxT = midT
        else:
            minT = midT+1
    return minT