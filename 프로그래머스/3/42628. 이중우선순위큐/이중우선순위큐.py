from heapq import heappush,heappop,_heapify_max,heapify
def solution(operations):
    answer = []
    q = []
    for i in operations:
        x,y = i.split(' ')
        if x == 'I':
            heappush(q,int(y))
        elif q: 
            if y == "-1":
                heappop(q)
            else:
                c = _heapify_max(q)
                heappop(q)
                heapify(q)
        else:
            pass
    if q:
        answer = [max(q),min(q)]
    else:
        answer = [0,0]
    return answer