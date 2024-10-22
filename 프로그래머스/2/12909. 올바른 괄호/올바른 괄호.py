def solution(s):
    
    count = 0
    
    for p in s:
        if p == "(":
            count += 1
        else:
            count -= 1
        if (count < 0):
            return False
    
    if count != 0:
        return False
        
    return True