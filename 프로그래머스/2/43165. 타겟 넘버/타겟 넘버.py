def solution(numbers, target):
    answer = [0]
    for num in numbers:
        temp = []
        for cal in answer:
            temp.append(cal + num)
            temp.append(cal - num)
        answer = temp
    return answer.count(target)