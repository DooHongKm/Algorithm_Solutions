def solution(s):
    
    numbers = list(map(int, s.split()))
    max_ = max(numbers)
    min_ = min(numbers)
        
    return f"{min_} {max_}"
    