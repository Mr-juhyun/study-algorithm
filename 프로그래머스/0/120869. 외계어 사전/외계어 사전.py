def solution(spell, dic):
    for word in dic:
        print(word)
        if sorted(word) == sorted(spell):
            print(sorted(word),sorted(spell))
            return 1
    return 2