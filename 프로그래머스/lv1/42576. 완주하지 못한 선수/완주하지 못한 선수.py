def solution(participant, completion):
    answer = ""
    dict_ = {}
    dict_2 = {}
    for p in participant:
        if p in dict_:
            dict_[p] += 1
        else:
            dict_[p] = 1   
    for c in completion:
        if c in dict_2:
            dict_2[c] += 1 
        else:
            dict_2[c] = 1
    for person in dict_:
        if person not in dict_2:
            answer = person
        elif dict_[person] > dict_2[person]:
            answer = person
    return answer