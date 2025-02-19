def solution(n, k, enemy):

    result = 0
    
    if k >= len(enemy):
        return len(enemy)
    
    left = k
    right = len(enemy)
    
    while left <= right:
        mid = (right - left) // 2 + left
        res = sum(sorted(enemy[:mid], reverse=True)[k:])
        if n >= res:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result
    
        