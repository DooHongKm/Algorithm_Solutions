def solution(places):
    return [checkAll(place) for place in places]
   
    
def checkAll(place):
    a = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    b1 = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    b2 = [[(1, 0), (0, 1)], [(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, -1)]]
    c1 = [(2, 0), (0, 2), (-2, 0), (0, -2)]
    c2 = a
    
    def check(person):
        x, y = person
        
        for dx, dy in a:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if place[ny][nx] == "P":
                return False
            
        for i in range(4):
            nx = x + b1[i][0]
            ny = y + b1[i][1]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue       
            if place[ny][nx] == "P":
                blocked = True
                for dx, dy in b2[i]:
                    bx = x + dx
                    by = y + dy
                    if place[by][bx] != "X":
                        blocked = False
                if not blocked:
                    return False
                
        for i in range(4):
            nx = x + c1[i][0]
            ny = y + c1[i][1]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue       
            if place[ny][nx] == "P":
                bx = x + c2[i][0]
                by = y + c2[i][1]
                if place[by][bx] != "X":
                    return False
        
        return True

    for j in range(5):
        for i in range(5):
            if place[j][i] == "P":
                if not check((i, j)):
                    return 0
                
    return 1