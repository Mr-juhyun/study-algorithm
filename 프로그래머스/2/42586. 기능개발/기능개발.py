def solution(progresses, speeds):
    answer = []
    def distribute(progresses):
        if progresses[0] >= 100:
            cnt.append(0)             
            del progresses[0]
            del speeds[0]
            if len(progresses) != 0:
                distribute(progresses)
            return len(cnt)

    while len(progresses) >0:
        cnt = []
        answer.append(distribute(progresses))
        progresses =  list(map(lambda x,y:x+y,progresses,speeds))
        
    return list(filter(lambda x:x!=None,answer))