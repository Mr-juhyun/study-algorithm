def solution(answers):
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    for idx,answer in enumerate(answers):
        if stu1[idx%5] == answer:
            scores[0] += 1
        if stu2[idx%8] == answer:
            scores[1] += 1
        if stu3[idx%10] == answer:
            scores[2] += 1
    high_score = max(scores)
    answer = []
    for i,v in enumerate(scores):
        if v == high_score:
            answer.append(i+1)
    return answer
   