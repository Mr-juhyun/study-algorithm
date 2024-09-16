def solution(n):
    def tower_of_hanoi(n,depart,arrive,remain):
        if n == 1:
            return [[depart,arrive]]
        else:
            return tower_of_hanoi(n-1,depart,remain,arrive) + [[depart,arrive]] + tower_of_hanoi(n-1,remain,arrive,depart)
    return tower_of_hanoi(n,1,3,2)