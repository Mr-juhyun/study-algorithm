def solution(sizes):
    larger = set()
    smaller = set()
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            larger.add(sizes[i][0])
            smaller.add(sizes[i][1])
        else:
            larger.add(sizes[i][1])
            smaller.add(sizes[i][0])
    result = max(larger) * max(smaller)
    return result