def solution(a, b):
    if a > b:
        h = a
        l = b
    else:
        h = b
        l = a
    return sum([i for i in range(l,h+1)])