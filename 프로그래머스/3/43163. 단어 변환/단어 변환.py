
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    words = deque(words)
    answer = 0
    while words:
        word = words.popleft()
        cnt = 0
        for i in range(len(word)):
            if word[i] != begin[i]:
                cnt += 1
        if cnt == 1:
            begin = word
            answer += 1
            if begin == target:
                return answer
            else:
                cnt = 0
                for i in range(len(target)):
                    if begin[i] != target[i]:
                        cnt += 1
                if cnt == 1:
                    return answer + 1
    return 0