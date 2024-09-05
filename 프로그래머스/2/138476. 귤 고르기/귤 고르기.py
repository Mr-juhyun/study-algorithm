from collections import Counter
def solution(k, tangerine):
    mandarins = Counter(tangerine)
    mandarins = sorted(mandarins.items(),key=lambda x:x[1],reverse = True)
    answer = 0
    for mandarin in mandarins:
        answer += 1
        if mandarin[1] >= k:
            return answer
        k -= mandarin[1]