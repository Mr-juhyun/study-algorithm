def solution(jobs):
    length = len(jobs)
    process_time = min(jobs)[0]
    jobs.sort(key = lambda x:x[1])
    jobs = {i:t for i,t in enumerate(jobs)}
    time = 0
    for _ in range(len(jobs)):
        x = 0
        for key in jobs:
            if jobs[key][0] <= process_time:
                process_time += jobs[key][1]
                x = 1
                break
        if x == 0:
            key = min(jobs,key=lambda x:jobs[x][0])
            process_time = sum(jobs[key])
        time += process_time - jobs[key][0] 
        jobs.pop(key)
    
    return time // length










