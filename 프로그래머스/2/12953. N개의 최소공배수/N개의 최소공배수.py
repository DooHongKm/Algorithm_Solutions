def solution(arr):
    
    result = 1
    
    while True:
        temp = True
        for a in arr:
            if result % a != 0:
                temp = False
                break
        if temp:
            return result
        result += 1