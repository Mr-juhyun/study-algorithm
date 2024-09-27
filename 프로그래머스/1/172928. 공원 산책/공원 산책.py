def solution(park, routes):
    direction = {'E':(0,1),'W':(0,-1),'S':(1,0),'N':(-1,0)}
    row = len(park)
    col = len(park[0])
    
    for r in range(row):
        for c in range(col):
            if park[r][c] == 'S':
                start = (r,c)
                break
    r,c = start
    park[r] = park[r].replace('S','O')
    for route in routes:
        d,n = route.split(' ')
        n = int(n)
        y,x = direction[d]
        check = True
        for i in range(1,n+1):
            ny,nx = y*i+r,x*i+c
            if 0<= ny < row and 0<= nx < col and park[ny][nx] == 'O':
                pass
            else:
                check = False
                break
        if check:
            r,c = ny,nx
            
    return [r,c]