from collections import deque
def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    b_weight = 0
    time = 0
    while trucks or b_weight > 0:
        b_weight -= bridge.popleft()
        time += 1
        if trucks and b_weight + trucks[0] <= weight:
            go = trucks.popleft()
            bridge.append(go)
            b_weight += go
        else:
            bridge.append(0)
    return time