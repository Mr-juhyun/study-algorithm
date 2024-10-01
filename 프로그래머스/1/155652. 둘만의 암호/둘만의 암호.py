def solution(s, skip, index):
    answer = ""
    skip = [ord(i) for i in skip]
    for char in s:
        cnt = 0
        trans = ord(char)
        while cnt < index:
            if trans == ord('z'):
                trans = ord('a')
            else:
                trans += 1
            if trans not in skip:
                cnt += 1
        answer+=chr(trans)
    return answer