def solution(bandage, health, attacks):
    max_heal = health
    cnt = 0
    result = 0
    for i in range(attacks[-1][0]+1):
        att = 0
        for j in attacks:
            if i == j[0]:
                att = 1
                health = health - j[1]
                cnt = 0
                if health <= 0:
                    result = -1
                    break
        if att == 0:    
            if health >= max_heal:
                health = max_heal
            else:
                health += bandage[1]
                cnt += 1
                if cnt == bandage[0]:
                    health += bandage[2]
                    cnt = 0
    if result != -1:
        result = health
    return result