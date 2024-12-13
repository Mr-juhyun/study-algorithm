from collections import defaultdict
def solution(s):
    answer = []
    temp = defaultdict()
    for i,v in enumerate(s):
        if v in temp:
            answer.append(i - temp[v])
            temp[v] = i
        else:
            answer.append(-1)
            temp[v] = i
    return answer