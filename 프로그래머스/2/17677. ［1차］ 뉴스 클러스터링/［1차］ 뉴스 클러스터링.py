from collections import Counter

def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    temp1 = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i+1].isalpha()]
    temp2 = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i+1].isalpha()]
    
    counter1 = Counter(temp1)
    counter2 = Counter(temp2)
    
    gyo = sum((counter1 & counter2).values())
    hap = sum((counter1 | counter2).values())
    if hap == 0:
        return 65536
    else:
        return int(gyo / hap * 65536)
    
    
    
    