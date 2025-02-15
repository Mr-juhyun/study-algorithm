def solution(schedules, timelogs, startday):
    answer = 0

    for idx,time in enumerate(schedules):
        day = startday
        h , m = divmod(time,100)
        m += 10
        if m >= 60:
            h += 1
            m -= 60
        h = str(h)
        m = str(m)
        if len(m) == 1:
            m = "0" + m
            
        go_to_work = int(h + m)
        
        for timelog in timelogs[idx]:
            if day <= 5:
                if timelog > go_to_work:
                    break
                    
            day += 1
            if day > 7: day = 1
                
        else: answer += 1 
    return answer