from collections import Counter 
def solution(id_list, report, k):
    report_list = {i:[] for i in id_list}
    reports = set(report)
    
    bad_users = []
    for r in reports:
        report_user, bad_user = r.split(' ')
        report_list[report_user].append(bad_user)
        bad_users.append(bad_user)
        
    target = [i for i in id_list if bad_users.count(i) >= k]
    answer = []
    for i in report_list:
        cnt = 0
        for r in report_list[i]:
            if r in target:
                cnt += 1
        answer.append(cnt)
    
    return answer