def solution(arr):
    n = len(arr)
    
    def quad(r_start, r_end, c_start, c_end):
        num = arr[r_start][c_start]  
        for row in range(r_start, r_end):
            for col in range(c_start, c_end):
                if arr[row][col] != num:  
                    
                    r_mid = (r_start + r_end) // 2
                    c_mid = (c_start + c_end) // 2
                    
                    quad1 = quad(r_start, r_mid, c_start, c_mid)
                    quad2 = quad(r_start, r_mid, c_mid, c_end)
                    quad3 = quad(r_mid, r_end, c_start, c_mid)
                    quad4 = quad(r_mid, r_end, c_mid, c_end)
                    
                    return [
                        quad1[0] + quad2[0] + quad3[0] + quad4[0],
                        quad1[1] + quad2[1] + quad3[1] + quad4[1]
                    ]
                    
        return [1, 0] if num == 0 else [0, 1]

    return quad(0, n, 0, n)