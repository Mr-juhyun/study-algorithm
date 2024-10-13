class Log:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def run(self,start_time,end_time):
        return self.start <= end_time and self.end >= start_time
        
from datetime import datetime, timedelta
def solution(lines):
    
    log_list = []
    
    for line in lines:
        _, end, run_time = line.split(' ')
        end = datetime.strptime(end,'%H:%M:%S.%f')
        start = end - timedelta(seconds = float(run_time[:-1]) - 0.001)
        log_list.append(Log(start,end))
        
    max_req = 0
    
    for now in log_list:
        start_time = now.end
        end_time = start_time + timedelta(seconds = 0.999)
        req = 0
        
        for log in log_list:
            if log.run(start_time,end_time):
                req += 1
        if req > max_req:
            max_req = req
        
    return max_req