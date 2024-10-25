def solution(elements):
    
    len_ = len(elements)
    sum_ = sum(elements)
    temp = [0 for i in range(sum_ + 1)]
    
    elements = elements + elements
    for i in range(1, len_ + 1):
        for j in range(len_):
            a = sum(elements[j:j+i])
            temp[a] = 1
    
    return temp.count(1)
    