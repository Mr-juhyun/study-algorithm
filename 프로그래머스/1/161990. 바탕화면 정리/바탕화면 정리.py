def solution(wallpaper):
    file = []
    for i in range(len(wallpaper)):
        raw = wallpaper[i]
        for j in range(len(raw)):
            column = raw[j]
            if column == '#':
                file.append([i,j])
    y = sorted(file,key=lambda x:x[0])
    x = sorted(file,key=lambda x:x[1])
    return [y[0][0],x[0][1],y[-1][0]+1,x[-1][1]+1]