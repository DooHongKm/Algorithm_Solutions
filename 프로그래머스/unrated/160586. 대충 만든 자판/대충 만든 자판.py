def solution(keymap, targets):
    answer = [0] * len(targets)
    key_dict = {}
    for k in keymap:
        for i in range(len(k)):
            temp = k[i]
            if temp in key_dict:
                key_dict[temp] = min(key_dict[temp], i + 1)
            else:
                key_dict[temp] = i + 1
    for i in range(len(targets)):
        count = 0
        for j in range(len(targets[i])):
            temp = targets[i][j]
            if temp in key_dict:
                count += key_dict[temp]
            else:
                count = -1
                break
        answer[i] = count
    return answer