def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    temp1 = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i+1].isalpha()]
    temp2 = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i+1].isalpha()]
    
    dict1 = {}
    dict2 = {}
    for t in temp1:
        if t in dict1:
            dict1[t] += 1
        else:
            dict1[t] = 1
    for t in temp2:
        if t in dict2:
            dict2[t] += 1
        else:
            dict2[t] = 1
            
    kyo = 0
    for key in dict1:
        if key in dict2:
            kyo += min(dict1[key], dict2[key])
            
    hap = len(temp1) + len(temp2) - kyo
    if hap == 0:
        return 65536
    else:
        return int(kyo / hap * 65536)
    