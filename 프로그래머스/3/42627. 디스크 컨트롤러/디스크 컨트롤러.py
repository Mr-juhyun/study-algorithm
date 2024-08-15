from heapq import heapify, heappop,heappush
def solution(jobs):
    process_time = min(jobs)[0]
    jobs = [[i[1],i[0]] for i in jobs]
    time = []
    
    for _ in range(len(jobs)):
        start = list(filter(lambda x:x[1] <= process_time,jobs))
        heapify(start)
        
        if start:
            minimum = heappop(start)
            process_time += minimum[0]
        else:
            minimum = min(jobs)
            process_time = sum(minimum)
            
        heappush(time,process_time - minimum[1])
        jobs.remove(minimum)

    return sum(time)//len(time)
