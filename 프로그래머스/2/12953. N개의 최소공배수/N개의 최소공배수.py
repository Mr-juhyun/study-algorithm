def find_LCM(x,y):
        if x == 1 or y == 1:
            return x*y
        for i in range(2,min([x,y])+1):
            f = divmod(x,i)
            s = divmod(y,i)
            if f[1] == 0 and s[1] == 0:
                return i * find_LCM(f[0],s[0])
        return x*y
    
def solution(arr):
    while len(arr) > 1:
        x = arr.pop()
        y = arr.pop()
        LCM = find_LCM(x,y)
        arr.append(LCM)
        
    return arr[0]