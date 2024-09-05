def solution(s):
    s = [char for char in s]
    s.sort(reverse=True)
    return ''.join(s)