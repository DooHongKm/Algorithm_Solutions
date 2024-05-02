def solution(skill, skill_trees):
    
    count = 0
    
    dic = {}
    for i, s in enumerate(skill):
        dic[s] = i
    
    for tree in skill_trees:
        temp = 0
        for t in tree:
            if t in dic and dic[t] != temp:
                count += 1
                break
            elif t in dic and dic[t] == temp:
                temp += 1
                
    answer = len(skill_trees) - count
    
    return answer