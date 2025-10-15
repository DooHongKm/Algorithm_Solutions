import copy


def rotate(array, height, width):
    
    r1 = [(i, height - j - 1) for j, i in array]
    r2 = [(height - j - 1, width - i - 1) for j, i in array]
    r3 = [(width - i - 1, j) for j, i in array]

    return [array, r1, r2, r3]
    
    
def solution(key, lock):
    
    key1 = [(i, j) for j in range(len(key)) for i in range(len(key)) if key[i][j] == 1]
    
    x_max = x_min = key1[0][1]
    y_max = y_min = key1[0][0]
    for j, i in key1[1:]:
        x_max = max(x_max, i)
        x_min = min(x_min, i)
        y_max = max(y_max, j)
        y_min = min(y_min, j)
        
    key_width = x_max - x_min + 1
    key_height = y_max - y_min + 1
        
    key1 = [(j - y_min, i - x_min) for j, i in key1]
    key_group = rotate(key1, key_height, key_width)
    
    for k in key_group:
        for j in range(1 - key_height, len(lock)):
            for i in range(1 - key_width, len(lock[0])):
                lock_copy = copy.deepcopy(lock)
                unfit = False
                for y, x in k:
                    if j + y < 0 or j + y >= len(lock) or i + x < 0 or i + x >= len(lock[0]):
                        continue
                    if lock_copy[j + y][i + x] == 1:
                        unfit = True
                        break
                    lock_copy[j + y][i + x] += 1
                if unfit:
                    continue
                if all(all(n == 1 for n in row) for row in lock_copy):
                    return True
    
    return False