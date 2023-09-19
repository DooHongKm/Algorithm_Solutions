def solution(s):
    answer = []
    alpha_dict = {}
    for i, alpha in enumerate(s):
        if alpha in alpha_dict:
            answer.append(i - alpha_dict[alpha])
            alpha_dict[alpha] = i
        else:
            answer.append(-1)
            alpha_dict[alpha] = i       
    return answer