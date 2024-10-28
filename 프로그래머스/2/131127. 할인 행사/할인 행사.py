def solution(want, number, discount):

    dict1 = {}
    for i in range(len(want)):
        dict1[want[i]] = number[i]
        
    count = 0
        
    for i in range(len(discount) - 9):
        dict2 = {}
        for j in range(10):
            if discount[i+j] in dict2:
                dict2[discount[i+j]] += 1
            else:
                dict2[discount[i+j]] = 1
        if dict1 == dict2:
            count += 1
            
    return count
        

            

            
            
        