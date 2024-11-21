def check(r, c, b):
    for t in b:
        m, n = t
        if c == n or r-c == m-n or r+c == m+n:
            return False
    return True
        
def solution(n):
    
    answer = 0
    stack = [(-1, [])]
    
    while stack:
        row, board = stack.pop()
        if row == n - 1:
            answer += 1
            continue
        for i in range(n):
            if check(row+1, i, board):
                temp = board + [(row+1, i)]
                stack.append((row+1, temp))
                
    return answer