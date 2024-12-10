def solution(genres, plays):

    answer = []
    
    dict_ = {}
    for idx, genre in enumerate(genres):
        if genre in dict_:
            dict_[genre][0] += plays[idx]
            dict_[genre].append((idx, plays[idx]))
        else:
            dict_[genre] = [plays[idx], (idx, plays[idx])]
    
    sorted_dict = sorted(dict_.items(), reverse=True, key=lambda x: x[1][0])
    for _, value in sorted_dict:
        sorted_value = sorted(value[1:], reverse=True, key=lambda x: x[1])
        for i in range(min(len(sorted_value), 2)):
            answer.append(sorted_value[i][0])
            
    return answer
        