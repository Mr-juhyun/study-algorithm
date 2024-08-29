def solution(A, B):
    B.sort()
    A.sort()
    idx = 0
    answer = 0
    for b in B:
        if b > A[idx]: 
            answer += 1
            idx += 1
    return answer