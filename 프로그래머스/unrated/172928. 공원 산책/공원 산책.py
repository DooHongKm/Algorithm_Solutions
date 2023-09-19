def solution(park, routes):
    x = 0
    y = 0
    w = len(park[0])
    h = len(park)
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                y = i
                x = j
                break
    print(y, x)
    for route in routes:
        xx = x
        yy = y
        direction = route[0]
        distance = int(route[2])
        if direction == "E" and 0 <= xx + distance < w:
            for i in range(distance):
                xx += 1
                if park[yy][xx] == "X":
                    xx = x
                    break
        elif direction == "W" and 0 <= xx - distance < w:
            for i in range(distance):
                xx -= 1
                if park[yy][xx] == "X":
                    xx = x
                    break
        elif direction == "S" and 0 <= yy + distance < h:
            for i in range(distance):
                yy += 1
                if park[yy][xx] == "X":
                    yy = y
                    break        
        elif direction == "N" and 0 <= yy - distance < h:
            for i in range(distance):
                yy -= 1
                if park[yy][xx] == "X":
                    yy = y
                    break 
        x = xx
        y = yy
        print(y, x)
    answer = [y, x]
    return answer