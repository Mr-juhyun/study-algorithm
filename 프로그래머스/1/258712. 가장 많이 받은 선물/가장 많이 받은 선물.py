def solution(friends, gifts):
    gift_list = {}
    for i in friends:
        gift_list[i] = {}
        for f in friends:
            gift_list[i][f] = 0
    
    for i in gifts:
        give,receive = i.split(' ')
        gift_list[give][receive] += 1
        gift_list[receive][give] -= 1
        gift_list[give][give] += 1
        gift_list[receive][receive] -=1
    
    answer = []
    for give in gift_list:
        will_receive = 0
        gift_score = gift_list[give][give]
        for receive in gift_list:
            if give == receive:
                pass
            else:
                if gift_list[give][receive] > 0:
                    will_receive += 1
                elif gift_list[give][receive] == 0:
                    if gift_score > gift_list[receive][receive]:
                        will_receive += 1
        answer.append(will_receive)
            
    
    return max(answer)