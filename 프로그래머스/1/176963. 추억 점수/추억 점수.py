from collections import defaultdict
def solution(name, yearning, photo):
    miss = defaultdict(int)
    answer = []
    
    for i,person in enumerate(name):
        miss[person] = yearning[i]
    
    for people in photo:
        miss_score = 0
        for person in people:
            if miss[person]:
                miss_score += miss[person]
        answer.append(miss_score)
    return answer