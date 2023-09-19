def solution(wallpaper):
    height = len(wallpaper)
    width = len(wallpaper[0])
    min_x = width - 1
    max_x = 0
    min_y = height - 1
    max_y = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            temp = wallpaper[i][j]
            if temp == "#":
                min_x = min(j, min_x)
                max_x = max(j, max_x)
                min_y = min(i, min_y)
                max_y = max(i, max_y)
    answer = [min_y, min_x, max_y + 1, max_x + 1]
    return answer