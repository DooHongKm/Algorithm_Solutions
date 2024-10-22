def solution(s):
    
    
    words = s.split(" ")
    answer = " ".join([word.capitalize() for word in words])
        
    return answer