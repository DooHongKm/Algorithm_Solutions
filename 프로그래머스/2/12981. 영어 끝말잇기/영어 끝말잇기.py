def solution(n, words):

    count = 0
    
    for i in range(len(words)):
        if i != 0:
            if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
                count = i
                break
     
    if count == 0:
        return [0, 0]
    a = count % n + 1
    b = count // n + 1
    return a, b
    
        