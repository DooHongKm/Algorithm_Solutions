from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

T = int(input())

for count in range(1, T + 1):
	
	n = int(input())
	graph = []
	for _ in range(n):
		graph.append(list(map(int, input())))
	temp = [[float('inf') for _ in range(n)] for _ in range(n)]
    
	q = deque([])
	q.append((0, 0))
	temp[0][0]=0
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			if nx<0 or ny<0 or nx>=n or ny>=n:
				continue
			else:
				nt = temp[y][x] + graph[ny][nx]
				if temp[ny][nx] > nt:  
					temp[ny][nx] = nt
					q.append((nx,ny))
                    
	print(f"#{count} {temp[n-1][n-1]}")