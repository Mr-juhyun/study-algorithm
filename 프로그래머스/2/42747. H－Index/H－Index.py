def solution(citations):
    for n in range(len(citations),-1,-1):
        h = list(filter(lambda x: x>=n,citations))
        if len(h) >= n:
            return n
        