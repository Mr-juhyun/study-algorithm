import heapq

class Scoville:
    def __init__(self, scoville, k):
        heapq.heapify(scoville)
        self.sco = scoville
        self.k = k
        self.count = 0
    def doNotMix(self):
        if self.sco[0] >= self.k:
            return 1
        else:
            return 0       
    def haveToMix(self):
        while self.doNotMix() == 0:
            if len(self.sco) < 2:
                return -1
        
            self.count += 1
            
            least = heapq.heappop(self.sco)
            
            secondLeast = heapq.heappop(self.sco)
            
            new = least + secondLeast * 2
            
            heapq.heappush(self.sco, new)
            
        return  self.count

def solution(scoville, k):
    sco = Scoville(scoville, k)
    answer = sco.haveToMix()

    return answer
