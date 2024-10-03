def solution(n, computers):
    answer = 0
    connect = set()
    def conn(now= 0):
        connect.add(now)
        for i,com in enumerate(computers[now]):
            if com and i not in connect:
                conn(i)
    for i in range(len(computers)):
        if i not in connect:
            conn(i)
            answer += 1
    return answer