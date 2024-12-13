def solution(k, score):
    answer = []
    hall_of_fame = []
    for i,s in enumerate(score):
        if i >= k:
            min_score = hall_of_fame[-1]
            if s > min_score:
                hall_of_fame.pop()
                hall_of_fame.append(s)
            else:
                pass
        else:
            hall_of_fame.append(s)
        hall_of_fame.sort(reverse=True)
        answer.append(hall_of_fame[-1])
            
    return answer