def solution(n, words):
    answer = []
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            if int((i+1)%n) == 0:
                answer.append(n)
            else:
                answer.append(int((i+1)%n))
            b = int((i+1)/n)
            if (i+1)%n == 0:
                answer.append(b)
                break
            else:
                answer.append(b+1)
                break
        elif words[i] in words[0:i]:
            if int((i+1)%n) == 0:
                answer.append(n)
            else:
                answer.append(int((i+1)%n))
            b = int((i+1)/n)
            if (i+1)%n == 0:
                answer.append(b)
                break
            else:
                answer.append(b+1)
                break
        
    if answer == []:
        answer.append(0)
        answer.append(0)
   


    return answer