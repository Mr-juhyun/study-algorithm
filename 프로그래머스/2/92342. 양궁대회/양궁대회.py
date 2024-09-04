def solution(n, info):
    
    def differ(ryan, apeach):
        diff = 0
        for idx in range(len(info)-1):
            score = 10 - idx
            if ryan[idx] > apeach[idx]:
                diff += score
            elif ryan[idx] < apeach[idx]:
                diff -= score
        return diff
    
    ryans_score = [[]]
    for apeach_shot in info:
        temp = []
        for ryan_shot in ryans_score:
            temp.append(ryan_shot + [0])
            if apeach_shot + 1 <= n:
                temp.append(ryan_shot + [apeach_shot + 1])
        ryans_score = temp

    ryans = []
    for ryan in ryans_score:
        if sum(ryan) <= n:
            ryan[-1] += (n - sum(ryan))
            ryan.append(differ(ryan,info))
            ryans.append(ryan)

    max_ryan = max(ryans, key=lambda x: x[-1])
    if max_ryan[-1] <= 0:
        return [-1]
    
    answer = list(filter(lambda x:x[-1] == max_ryan[-1],ryans))
    answer.sort(key=lambda x: x[::-1],reverse=True)
    
    return answer[0][:-1]