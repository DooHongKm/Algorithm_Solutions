def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    a = [str1[i:i+2] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    b = [str2[i:i+2] for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    la = len(a)
    lb = len(b)

    gyo = 0
    for i in a:
        if i in b:
            b.remove(i)
            gyo += 1
    hap = la + lb - gyo
    
    if hap == 0:
        result = 65536
    else:
        result = int(gyo / hap * 65536)
    
    return result