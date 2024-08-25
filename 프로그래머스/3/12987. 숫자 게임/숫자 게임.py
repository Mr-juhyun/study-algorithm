from heapq import heapify, heappop, heappush
def solution(A, B):
    heapify(A)
    heapify(B)
    answer = 0
    while B:
        target_a = heappop(A)
        target_b = heappop(B)
        if target_b > target_a:
            answer += 1
        else:
            heappush(A,target_a)
    return answer