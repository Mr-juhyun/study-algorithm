from collections import defaultdict
def solution(keymap, targets):
    keyboard = {}
    for key in keymap:
        for i,k in enumerate(key):
            keyboard.setdefault(k,101)
            if keyboard[k] > i+1:
                keyboard[k] = i+1
    result = []
    for target in targets:
        cnt = 0
        for t in target:
            try:
                cnt += keyboard[t]
            except:
                cnt = -1
                break
        result.append(cnt)
    return result