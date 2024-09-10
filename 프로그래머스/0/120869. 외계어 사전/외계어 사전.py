from itertools import permutations
def solution(spell, dic):
    spell = permutations(spell,len(spell))
    for per_spell in spell:    
        for word in dic:
            target = str(''.join(per_spell))
            if word == target:
                return 1
    return 2