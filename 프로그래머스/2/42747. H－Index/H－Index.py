def solution(citations):

    a = len(citations)
    b = max(citations)
    i = min(a, b)
    
    while True:
        count = 0
        for citation in citations:
            if citation >= i:
                count += 1
        if count >= i:
            break
        else:
            i -= 1
            continue
            
    return i