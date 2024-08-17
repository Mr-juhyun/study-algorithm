from collections import Counter
import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    answer = 0
    works = list(map(lambda x:-x,works))
    heapq.heapify(works)
    for _ in range(n):
        max_work = heapq.heappop(works)
        max_work += 1
        heapq.heappush(works,max_work)
        
    works = Counter(works)
    for work in works:
        answer += work**2 * works[work]
    return answer
