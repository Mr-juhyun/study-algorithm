from collections import deque
class Picks:
    def __init__(self,picks):
        self.diamond = picks[0]
        self.iron = picks[1]
        self.stone = picks[2]
        
    def diamond_pick(self,minerals):
        tired = len(minerals)
        return tired
    
    def iron_pick(self,minerals):
        tired = 0
        for m in minerals:
            if m == "diamond":
                tired += 5
            else : tired += 1
        return tired
    
    def stone_pick(self,minerals):
        tired = 0
        for m in minerals:
            if m =="diamond":
                tired += 25
            elif m == "iron":
                tired += 5
            else:
                tired += 1
        return tired 
        
    def mining(self,minerals):
        if self.diamond != 0:
            self.diamond -= 1
            return self.diamond_pick(minerals)
        
        elif self.iron != 0:
            self.iron -= 1
            return self.iron_pick(minerals)
        
        else:
            self.stone -= 1
            return self.stone_pick(minerals)
        
            
def solution(picks, minerals):
    num = min(sum(picks)*5,len(minerals))
    start = 0
    end = 5
    five_minerals = []
    
    while start < num:
        five_minerals.append(minerals[start:end])
        start += 5
        end += 5
        
    minerals = deque(sorted(five_minerals, key = lambda x:(x.count('diamond'),x.count('iron')),reverse=True))
    
    p = Picks(picks)
    
    answer = 0
    
    while minerals:
        temp = minerals.popleft()
        answer += p.mining(temp)
                
    return answer