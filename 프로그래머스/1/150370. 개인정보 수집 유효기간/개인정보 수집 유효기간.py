def trans2day(date):
    y,m,d = date.split('.')
    return int(y)*12*28 + (int(m)-1)*28 + int(d)
    
def solution(today, terms, privacies):
    today = trans2day(today)
    target = {}
    answer = []
    for t in terms:
        i,v = t.split()
        target[i] = int(v)
        
    for i,p in enumerate(privacies):
        date,v = p.split(" ")
        if trans2day(date) + target[v]*28 <= today:
            answer.append(i+1)
    return answer