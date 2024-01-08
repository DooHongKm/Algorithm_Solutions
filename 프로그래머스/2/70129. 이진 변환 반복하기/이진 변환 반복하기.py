def solution(s):
    
    answer = []
    t = 0
    r = 0
    x = s
    
    while(x != '1'):
        one = 0
        for i in x:
            if i == '1':
                one += 1
            else:
                r += 1
        x = bin(one)[2:]
        print(x)
        t += 1
    answer.append(t)
    answer.append(r)
    
    return answer
            
    
    
    
    
    
    
    
    
    
    
    return answer