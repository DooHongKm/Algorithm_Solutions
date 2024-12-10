def solution(arr):
    
    temp = [0, 0]
    
    def check(x, y, n):
        nonlocal temp
        if n == 1:
            temp[arr[y][x]] += 1
            return
        number = arr[y][x]
        for i in range(n):
            for j in range(n):
                if arr[y + i][x + j] != number:
                    check(x, y, n//2)
                    check(x+n//2, y, n//2)
                    check(x, y+n//2, n//2)
                    check(x+n//2, y+n//2, n//2)
                    return
        temp[number] += 1
        
    check(0, 0, len(arr))
    return temp
            
