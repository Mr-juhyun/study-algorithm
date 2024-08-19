def solution(s):
    temp = 0
    for char in s:
        if char == '(':
            temp += 1
        else:
            temp -= 1
        if temp == -1:
            return False
    if temp == 0:
        answer = True
    else:
        answer = False
    return answer