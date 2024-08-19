from collections import deque

def solution(priorities, location):
    want = {location:priorities[location]}
    key = deque([key for key in range(len(priorities))])
    value = deque([value for value in priorities])
    cnt = 0
    
    while True:
        if max(value) == value[0]:
            temp_val = value.popleft()
            temp_key = key.popleft()
            cnt += 1
            if {temp_key:temp_val} == want:
                return cnt
        else:
            key.rotate(-1)
            value.rotate(-1)