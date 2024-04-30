def solution(dirs):
    
    stack = [(0, 0)]
    
    dir_dict = {}
    dir_dict['U'] = (0, 1)
    dir_dict['D'] = (0, -1)
    dir_dict['R'] = (1, 0)
    dir_dict['L'] = (-1, 0)
    
    x = 0
    y = 0
    for d in dirs:
        x = max(min(x + dir_dict[d][0], 5), -5)
        y = max(min(y + dir_dict[d][1], 5), -5)
        if (x, y) != stack[-1]:
            stack.append((x, y))
            
    paths = set()
    for i in range(len(stack)-1):
        paths.add(stack[i] + stack[i + 1])
        paths.add(stack[i + 1] + stack[i])
            
    answer = len(paths) // 2
    
    return answer
    