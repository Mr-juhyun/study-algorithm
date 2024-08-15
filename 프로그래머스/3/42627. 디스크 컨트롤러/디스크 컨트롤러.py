def solution(jobs):
    process_time = min(jobs)[0]
    jobs = sorted(jobs,key=lambda x:x[1])
    time = []
    for _ in range(len(jobs)):
        x = 0
        for disk in jobs:
            if disk[0] <= process_time:
                process_time += disk[1]
                x = 1
                break
        if x == 0:
            disk = min(jobs)
            process_time = sum(disk)
        time.append(process_time - disk[0])   
        jobs.remove(disk)
    
    return sum(time)//len(time)
