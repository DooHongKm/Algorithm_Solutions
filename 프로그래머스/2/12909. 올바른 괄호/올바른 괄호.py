def solution(s):
    
    count = 0
    result = True
    
    for temp in s:
        if temp == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            result = False
            break
    if count != 0:
        result = False

    return result