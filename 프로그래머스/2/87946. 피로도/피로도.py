from itertools import permutations
def solution(k, dungeons):
    max_enters = len(dungeons)
    dungeons = permutations(dungeons,max_enters)
    answer = 0
    for dungeon in dungeons:
        cnt = 0
        full_k = k
        for d in dungeon:
            enter = d[0]
            consume = d[1]
            if d[0] > full_k or full_k < 1:
                break
            full_k -= consume
            cnt +=1
        if answer < cnt:
            answer = cnt
    return answer