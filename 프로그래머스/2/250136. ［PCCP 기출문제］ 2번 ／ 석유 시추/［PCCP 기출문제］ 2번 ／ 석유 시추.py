from collections import deque,defaultdict

def oil_location(land,n,m,row,col,visited):
    
    q = deque([(row,col)])
    visited.add((row,col))
    col_list = set([col])
    oil = 1
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while q:
        y,x = q.popleft()
        
        for dy,dx in direction:
            ny,nx = dy+y,dx+x
            
            if 0<= ny < n and 0<= nx < m and (ny,nx) not in visited:
                if land[ny][nx]:
                    
                    visited.add((ny,nx))
                    q.append((ny,nx))
                    oil += 1
                    col_list.add(nx)
                    
    return oil, col_list
    
def solution(land):
    
    n = len(land)
    m = len(land[0])
    visited = set()
    oil_list = defaultdict(int)
    
    for row in range(n):
        for col in range(m):
            if land[row][col] and (row,col) not in visited:
                
                oil, col_list = oil_location(land,n,m,row,col,visited)
                
                for col in col_list:
                    oil_list[col] += oil
                    
    return max(oil_list.values())