def solution(clothes):
    
    result = 1
    dict_ = {}
    
    for c in clothes:
        temp = c[1]
        if temp in dict_:
            dict_[temp] += 1
        else:
            dict_[temp] = 1
            
    for d in dict_:
        temp = dict_[d] + 1
        result *= temp
        
    result -= 1
    
    return result