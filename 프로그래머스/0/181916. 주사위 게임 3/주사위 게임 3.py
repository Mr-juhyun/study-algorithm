from collections import Counter
def solution(a, b, c, d):
    dice = Counter([a,b,c,d])
    dice = sorted(dice.items(),key=lambda x:-x[1])
    max_dice,max_cnt = dice[0]
    if max_cnt == 4:
        return max_dice * 1111
    elif max_cnt == 3:
        return (10*max_dice + dice[1][0])**2
    elif max_cnt == 2 and len(dice) == 2:
        return (max_dice+dice[1][0]) * abs(max_dice - dice[1][0])
    elif max_cnt == 2 and len(dice) == 3:
        return dice[1][0] * dice[2][0]
    else:
        return min(a,b,c,d)