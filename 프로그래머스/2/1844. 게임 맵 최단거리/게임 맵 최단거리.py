def solution(maps):
    n = len(maps)-1     
    m = len(maps[0])-1 
    
    
    going = [[0, 0, 1]]

    while going:
        next_going = []  
        for x, y, cnt in going:
    
            if x == n  and y == m :
                return cnt

            
            # 상
            if x - 1 >= 0 and maps[x - 1][y] == 1:
                maps[x - 1][y] = 0 
                next_going.append((x - 1, y, cnt + 1))

            # 하
            if x + 1 <= n and maps[x + 1][y] == 1:
                maps[x + 1][y] = 0  
                next_going.append((x + 1, y, cnt + 1))

            # 좌
            if y - 1 >= 0 and maps[x][y - 1] == 1:
                maps[x][y - 1] = 0  
                next_going.append((x, y - 1, cnt + 1))

            # 우
            if y + 1 <= m and maps[x][y + 1] == 1:
                maps[x][y + 1] = 0  
                next_going.append((x, y + 1, cnt + 1))
        
        going = next_going  
    
    
    return -1
