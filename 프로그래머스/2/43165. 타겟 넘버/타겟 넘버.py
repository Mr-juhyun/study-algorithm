from collections import deque
def solution(numbers, target):
    numbers = deque(numbers)
    answer = [0]
    while numbers:
        num = numbers.popleft()
        temp = []
        for i in answer:
            temp += [i+num]
            temp += [i-num]
        answer = temp
    return answer.count(target)