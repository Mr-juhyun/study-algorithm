def mod(x,y):
    a = min(x,y)
    b = max(x,y)
    if a == 0:
        return b
    return mod(a,b%a)

def solution(arr):
    lcm = arr[0]
    for n in arr[1:]:
        lcm = lcm*n//mod(lcm,n)
        
    return lcm