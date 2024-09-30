def solution(maze):
    walls = []
    rows = len(maze)
    cols = len(maze[0])

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                red_start = [r, c]
            elif maze[r][c] == 2:
                blue_start = [r, c]
            elif maze[r][c] == 3:
                red_end = [r, c]
            elif maze[r][c] == 4:
                blue_end = [r, c]
            elif maze[r][c] == 5:
                walls.append([r, c])

    red_paths = [] 
    blue_paths = [] 
    def bfs(now, end, color, path):
        
        if now == end:
            color.append(path)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for y, x in directions:
            ny = now[0] + y
            nx = now[1] + x
            
            if 0 <= ny < rows and 0 <= nx < cols and [ny, nx] not in path and [ny, nx] not in walls:
                bfs([ny, nx], end, color, path + [[ny, nx]])
                
    bfs(red_start, red_end, red_paths, [red_start])
    bfs(blue_start, blue_end, blue_paths, [blue_start])
    
    if not red_paths or not blue_paths:
        return 0
    times = []
    for r_path in red_paths:
        for b_path in blue_paths:
            time = 0
            check = True
            r_now = r_path[0]
            b_now = b_path[0]
            for i in range(1,max(len(r_path),len(b_path))):
                r_next = r_path[i] if i < len(r_path) else r_now
                b_next = b_path[i] if i < len(b_path) else b_now
                if r_next == b_next or (r_next == b_now and b_next == r_now):
                    check = False
                    break
                r_now = r_next
                b_now = b_next
                time += 1
            if check:
                times.append(time)
    if not times:
        return 0
    else:
        return min(times) 