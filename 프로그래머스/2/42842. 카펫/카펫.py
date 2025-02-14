def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(3,int(total**0.5)+1):
        if total%i == 0:
            x = total //i
            y = i
            if (x-2) * (y-2) == yellow:
                answer = [x,y]
                break
    
    return answer