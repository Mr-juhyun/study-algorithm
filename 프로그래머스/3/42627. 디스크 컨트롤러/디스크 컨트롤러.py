from collections import deque
def solution(jobs):
    jobs = deque(jobs)
    time = []
    process_time = min(jobs)[0]
    for _ in range(len(jobs)):
        try:
            start = min(filter(lambda x:x[0]<=process_time,jobs),key=lambda x:x[1])
            process_time += start[1]
        except:
            start = min(jobs) 
            process_time = start[0]+start[1]
        time.append(process_time - start[0])
        jobs.remove(start)
    
    return sum(time)//len(time) 