def solution(prices):
    
    stack = []
    result = [0] * len(prices)
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
        
    while stack:
        idx = stack.pop()
        result[idx] = len(prices) - idx - 1
        
    return result