def solution(board):
    n = len(board)
    def find_location(column,raw,location):
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        for x,y in directions:
            nx,ny = column+x,raw+y
            if 0<=nx<n and 0<= ny < n and board[ny][nx] == 0: 
                location.add((ny,nx))
    location = set()
    for raw in range(n):
        for column in range(n):
            if board[raw][column]:
                location.add((raw,column))
                find_location(column,raw,location)
    return n*n - len(location)
                   