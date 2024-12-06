def solution(skill, skill_trees):
    
    answer = len(skill_trees)
    
    for skill_tree in skill_trees:
        temp = ""
        for s in skill_tree:
            if s in skill:
                temp += s
        idx = 0
        for t in temp:
            if t == skill[idx]:
                idx += 1
            else:
                answer -= 1
                break
                
    return answer
            