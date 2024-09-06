import re
from itertools import permutations,combinations

def solution(user_id, banned_id):
    banned_id = [i.replace('*', '.') for i in banned_id]
    answer= set()
    all_user = permutations(user_id,len(banned_id))
    for user in all_user:
        cnt = 0
        for i in range(len(banned_id)):
            if len(user[i]) == len(banned_id[i]) and re.match(banned_id[i],user[i]):
                cnt +=1
        if cnt == len(banned_id):    
            answer.add(tuple(sorted(user)))
    return len(answer)