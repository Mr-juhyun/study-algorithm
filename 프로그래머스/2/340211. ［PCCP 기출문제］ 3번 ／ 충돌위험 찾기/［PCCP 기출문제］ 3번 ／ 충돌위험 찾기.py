from collections import deque, Counter

class RobotRoute:
    def __init__(self, robot):
        self.robot = robot
        self.start = self.robot.popleft()  
        self.end = self.robot.popleft()    
        self.route = []                    

    def move(self):
        while True:
            self.route.append(tuple(self.start))  
            
            
            if self.start[0] > self.end[0]:
                self.start[0] -= 1
            elif self.start[0] < self.end[0]:
                self.start[0] += 1
     
            elif self.start[1] > self.end[1]:
                self.start[1] -= 1
            elif self.start[1] < self.end[1]:
                self.start[1] += 1
            
            if self.start == self.end:
                if self.robot:
                    self.end = self.robot.popleft()
                else:
                    break
        self.route.append(tuple(self.end))
        return self.route

def solution(points, routes):
    robot = []
    cnt = 0

    for route in routes:
        robot.append(deque([points[i-1].copy() for i in route]))
    full_route = []
    for route in robot:
        r = RobotRoute(route)
        full_route.append(deque(r.move()))
    while any(full_route):
        temp = []
        for route in full_route:
            if route: 
                temp.append(route.popleft()) 
        
        for count in Counter(temp).values():
            if count > 1: 
                cnt += 1

    return cnt