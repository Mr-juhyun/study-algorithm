import re
def solution(babbling):
    
    def x(ba,speak):
        for sp in speak:
            
            if re.match(sp,ba):
                if sp == ba: return True
                
                ba = ba[len(sp):]
                speak.remove(sp)
                if not speak: return False
                return x(ba,speak)
        return False
    
    can_speak = ["aya", "ye", "woo", "ma"]
    answer = 0
    for ba in babbling:
        
        speak = can_speak.copy()
        
        if x(ba,speak): answer += 1
            
    return answer