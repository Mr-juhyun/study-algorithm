def solution(n, m, section):
    cnt = 0
    done = 0
    for s in section:
        if s > done:
            cnt += 1
            done = s+m-1
    return cnt