def solution(A, B):

    result = 0
    
    A.sort()
    B.sort()

    idx = 0
    fin = False
    for a in A:
        while a >= B[idx]:
            idx += 1
            if idx == len(B):
                fin = True
                break
        if fin:
            break
        result += 1
        idx += 1
        if idx == len(B):
            break
            
    return result
        