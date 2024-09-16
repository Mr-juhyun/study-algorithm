from collections import Counter
from itertools import combinations
def solution(clothes):
    answer = 1
    clothes = Counter(clothes:= [cloth[1] for cloth in clothes])
    for idx in clothes: answer *= (clothes[idx] + 1)
    return answer - 1