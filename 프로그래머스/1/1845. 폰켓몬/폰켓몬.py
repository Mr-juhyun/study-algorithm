# def solution(nums):
#     cnt = set(nums)
#     if len(nums)/2 > len(cnt):
#         answer = len(cnt)
#     else:
#         answer = len(nums)/2
#     return answer

def solution(nums):
    return min([len(set(nums)),len(nums)/2])