def solution(s):
    
    numbers = list(map(int, s.split()))
    max_ = max(numbers)
    min_ = min(numbers)
    answer = f"{min_} {max_}"
    
    return answer