def solution(s):
    
    result = ""
    temp = s.split(' ')

    for t in temp:
        result += t.capitalize() + ' '
    result = result[:-1]
    
    return result