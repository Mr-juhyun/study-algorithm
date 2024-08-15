def solution(jobs):
    process_time = 0
    result_time = 0
    length = len(jobs)
    jobs = sorted(jobs,key=lambda x:x[1])
    for _ in range(length):
        x = 0
        for disk in jobs:
            if disk[0] <= process_time:
                process_time += disk[1]
                x = 1
                break
        if x == 0:
            disk = min(jobs)
            process_time = sum(disk)
        result_time += process_time - disk[0]
        jobs.remove(disk)
    
    return result_time//length











