def solution(routes):
    
    answer = 1
    
    routes.sort()
    temp = routes[0]
    for route in routes[1:]:
        if temp[1] >= route[0]:
            temp = [route[0], min(route[1], temp[1])]
        else:
            temp = route
            answer += 1
    
    return answer
        
    
                