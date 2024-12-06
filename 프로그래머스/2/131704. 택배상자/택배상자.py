def solution(order):

    result = 0
    
    stack = []
    first_item = 1
    
    for o in order:
        if o > first_item:
            stack += [i for i in range(first_item, o)]
            first_item = o + 1
            result += 1
        elif o < first_item:
            if stack[-1] == o:
                stack.pop()
                result += 1
            else:
                break
        else:
            first_item = o + 1
            result += 1
    
    return result
                
        