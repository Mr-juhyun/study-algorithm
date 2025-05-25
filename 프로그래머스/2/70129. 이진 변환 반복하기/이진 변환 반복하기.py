def solution(s):
    s = [int(i) for i in s]
    zero = 0
    turn = 0
    while len(s) > 1:
        zero += s.count(0)
        s = len(s) - s.count(0)
        temp = []
        while s > 1:
            temp.insert(0,s%2)
            s = s//2
        temp.insert(0,1)
        s = temp
        turn += 1
    return [turn,zero]