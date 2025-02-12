from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices[:-1])
    while prices:
        time = 1
        now = prices.popleft()
        for target in prices:
            if now > target:
                break
            else:
                time += 1
        answer.append(time)
    return answer+[0]