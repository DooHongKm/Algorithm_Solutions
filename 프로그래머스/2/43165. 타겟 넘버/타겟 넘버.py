def solution(numbers, target):

    answer = 0
    l = len(numbers)
    
    def dfs(idx, value):
        nonlocal answer
        if idx == l: 
            if value == target:
                answer += 1
            return
        number = numbers[idx]
        dfs(idx + 1, value + numbers[idx])
        dfs(idx + 1, value - numbers[idx])
        
    dfs(0, 0)
    return answer