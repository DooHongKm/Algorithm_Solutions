def solution(begin, target, words):
    
    answer = 0
    stack = [(0, begin)]
    used = []
    
    while stack:
        idx, cur = stack.pop()
        if cur == target:
            if answer == 0:
                answer = idx
            else:
                answer = min(answer, idx)
        for word in words:
            count = 0
            for i, w in enumerate(word):
                if w != cur[i]:
                    count += 1
            if count == 1 and word not in used:
                stack.append((idx + 1, word))
                used.append(word)
                
    return answer   