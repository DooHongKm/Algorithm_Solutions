def solution(name, yearning, photo):
    info = {}
    answer = []
    for i in range(len(name)):
        info[name[i]] = yearning[i]
    for p in photo:
        score = 0
        for person in p:
            if person in info:
                score += info[person]
        answer.append(score)
    return answer