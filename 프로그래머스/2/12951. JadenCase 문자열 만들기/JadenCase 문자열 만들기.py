def solution(s):
    word = s.split(' ')
    answer = []
    for a in word:
        if a:
            string = a[0].upper() + a[1:].lower()
        else:
            string = a
        answer.append(string)
    return " ".join(answer)