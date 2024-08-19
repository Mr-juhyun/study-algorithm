def solution(progresses, speeds):
    answer = []
    idx = 0
    cnt = 0
    while idx < len(progresses):
        if progresses[idx] >= 100:
            cnt += 1
            idx +=1
        else:
            progresses = list(map(lambda x,y:x+y,progresses,speeds))
            if cnt != 0:
                answer.append(cnt)
            cnt = 0
    answer.append(cnt)
    return answer           