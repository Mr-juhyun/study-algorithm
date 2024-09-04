def solution(n, info):
    ryan_score = [[n,0]]
    max_difference = 0
    for idx in range(len(info)):
        apeach_shot = info[idx]
        temp = []
        score = 10-idx
        for ryan_shot in ryan_score:
            diff = ryan_shot.pop()
            if idx == 10:
                if diff >= max_difference: 
                    temp.append(ryan_shot + [ryan_shot[0]]+[diff])
                    max_difference = diff
            else:
                if apeach_shot > 0:
                    diff -= score
                    temp.append(ryan_shot +[0]+[diff])
                    diff += score
                else:
                    temp.append(ryan_shot +[0]+[diff])
                if apeach_shot + 1 <= ryan_shot[0]:
                    diff += score
                    ryan_shot[0] -= apeach_shot +1 
                    temp.append(ryan_shot + [apeach_shot+1]+[diff])
        
        ryan_score = temp
    ryan_score.sort(key=lambda x: x[::-1],reverse=True)
    if not ryan_score or ryan_score[0].pop() <= 0:
        return [-1]
    return ryan_score[0][1:]