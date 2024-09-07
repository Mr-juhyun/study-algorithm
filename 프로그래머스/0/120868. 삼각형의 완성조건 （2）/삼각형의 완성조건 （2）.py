def solution(sides):
    long_side = max(sides)
    short_side = min(sides)
    answer = set()
    for i in range(long_side - short_side+1,long_side+1):
        answer.add(i)
    for i in range(long_side,long_side+short_side):
        answer.add(i)
    return len(answer)