def solution(numbers):
    hot = sorted(list(map(str, numbers)),reverse=True, key=lambda x: x*4)
    if max(hot) == '0':
        return '0'
    answer = ''
    for i in hot:answer += i
    return answer