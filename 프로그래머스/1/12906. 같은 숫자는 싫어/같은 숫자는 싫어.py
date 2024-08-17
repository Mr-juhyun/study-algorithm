def solution(arr):
    x = [arr[i] for i in range(len(arr)-1) if arr[i] != arr[i+1]]
    x.append(arr[-1])
    return x