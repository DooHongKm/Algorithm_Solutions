from itertools import product

def solution(word):
    
    temp = list(product(["A", "E", "I", "O", "U", ""], repeat=5))
    
    dict_ = [""] * len(temp)
    for i in range(len(temp)):
        dict_[i] = "".join(temp[i])
        
    dict_ = sorted(list(set(dict_)))

    return dict_.index(word)
    
    

        