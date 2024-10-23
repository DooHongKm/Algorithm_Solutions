def solution(s):

    countT = 0
    count0 = 0
    
    while True:
        if (s == "1"):
            break
        count0 += s.count("0")
        temp = s.replace("0", "")
        temp2 = len(temp)
        temp3 = bin(temp2)[2:]
        s = temp3
        countT += 1
        
    return countT, count0
        
        
        