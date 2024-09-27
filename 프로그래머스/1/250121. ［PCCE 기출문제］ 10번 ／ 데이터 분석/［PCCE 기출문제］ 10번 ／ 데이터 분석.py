def solution(data, ext, val_ext, sort_by):
    answer = []
    analyze = {'code':0,'date':1,'maximum':2,'remain':3}
    return sorted(list(filter(lambda x:x[analyze[ext]] < val_ext,data)),key=lambda x:x[analyze[sort_by]])      