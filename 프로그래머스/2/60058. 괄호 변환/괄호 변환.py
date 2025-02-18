# 올바른 괄호 문자열인지 체크하는 함수
# 올바르면 -1, 올바르지 않으면 idx를 반환
def check(string):
    
    idx = -1
    count = 0
    right = True
    
    for i, s in enumerate(string):
        if s == "(":
            count += 1
        else:
            count -= 1
        if count == 0 and idx < 0:
            idx = i + 1
        if count < 0:
            right = False
        if not right and idx > 0:
            break
            
    return -1 if right else idx

    

# 변환 함수
def transform(string):

    if len(string) == 0:
        return ""
    
    idx = check(string)
    if idx == -1:
        return string
        
    u = string[:idx]
    v = string[idx:]
    
    if check(u) < 0:
        return u + transform(v)
    
    temp = "".join(["(" if p == ")" else ")" for p in u[1:-1]])
    return "(" + transform(v) + ")" + temp


# 주 함수
def solution(p):
    
    return transform(p)
    
    
        

    