def solution(n, computers):
    answer = 0
    connect = []
    
    def net(comNumber):
        connect.append(comNumber)
        
        for i in range(n):
            if i not in connect and computers[comNumber][i] == 1:
                net(i)
                
    for i in range(n):
        if i not in connect:
            net(i)
            answer+=1
    return answer