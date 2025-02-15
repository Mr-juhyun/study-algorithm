from itertools import combinations
def solution(n, q, ans):
    answer = 0
    nums = [i for i in range(1,n+1)]
    useless = []
    
    for idx,a in enumerate(ans):
        if a == 0: 
            useless.extend(q[idx])
            q[idx] = 0
            
    ans = list(filter(lambda x: x!=0,ans))
    q = list(filter(lambda x:x!=0,q))
    
    for l in set(useless): nums.remove(l)
    
    for try_list in combinations(nums,5):
        for idx,in_q in enumerate(q):
            correct = 0
            for t in try_list:
                if t in in_q:
                    correct += 1
            if correct != ans[idx]:
                break
        else: answer += 1
            
    return answer