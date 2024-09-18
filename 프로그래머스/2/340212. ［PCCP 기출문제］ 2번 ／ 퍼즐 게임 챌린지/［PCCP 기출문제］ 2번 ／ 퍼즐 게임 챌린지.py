def solution(diffs, times, limit):
    max_level,min_level = max(diffs),1
    
    while max_level > min_level:
        level = (max_level+min_level)//2
        time = 0

        for i in range(len(diffs)):
            if i == 0:
                time_prev = 0
            else:
                time_prev = times[i-1]
                
            time_cur = times[i]
            diff = diffs[i] - level
            
            if diff <= 0:
                time += time_cur
            else:
                time += (time_cur+time_prev)*diff+time_cur
                
        if time > limit:
            min_level = level+1
        else:
            max_level = level
            
    return min_level
