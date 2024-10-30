def solution(info, edges):
    visited = set()
    answer = []
    
    def max_sheep(sheep = 1,wolf = 0,now = 0):
        visited.add(now)
        if sheep <= wolf:
            return 0
        else:
            answer.append(sheep)
            
        #parent node, child node    
        for pn , cn in edges:
            if pn in visited and cn not in visited:
                if info[cn] == 1:
                    max_sheep(sheep,wolf+1,cn)
                else:
                    max_sheep(sheep+1,wolf,cn)
                visited.remove(cn)
    max_sheep()
    return max(answer)