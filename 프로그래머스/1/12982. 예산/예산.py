from heapq import heapify,heappop
def solution(d, budget):
    answer = 0
    heapify(d)
    while d:
        least = heappop(d)
        if least > budget:
            break
        budget -= least
        answer += 1
    return answer