for i in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))

    answer = 0
    for j in range(n - 4):
        temp = buildings[j:j+5]
        if temp[2] != max(temp):
            continue
        else:
            sTemp = sorted(temp, reverse=True)
            answer += (sTemp[0] - sTemp[1])
    
    print(f"#{i} {answer}")
            
            
        
        