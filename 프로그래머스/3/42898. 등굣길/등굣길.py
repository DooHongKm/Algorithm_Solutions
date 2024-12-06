def solution(m, n, puddles):

    
    roads = [[0 for _ in range(m)] for _ in range(n)]
    roads[0][0] = 1
    for i in range(1, m):
        if [i+1, 1] in puddles:
            roads[0][i] = 0
        else:
            roads[0][i] = roads[0][i-1]
    for i in range(1, n):
        if [1, i+1] in puddles:
            roads[i][0] = 0
        else:
            roads[i][0] = roads[i-1][0]

    for y in range(1, n):
        for x in range(1, m):
            if [x+1, y+1] in puddles:
                roads[y][x] = 0
                continue
            roads[y][x] = roads[y][x-1] + roads[y-1][x]        
            
    return roads[n-1][m-1] % 1000000007