def solution(n):
    answer = []
    triangle = [[0]*i for i in range(1,n+1)]
    num = 1
    row,col = -1,0
    
    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0:
                row += 1
            elif i %3 == 1:
                col += 1
            else:
                row-=1
                col-=1
            triangle[row][col] = num
            num += 1
    
    answer = [j for i in triangle for j in i]
    return answer