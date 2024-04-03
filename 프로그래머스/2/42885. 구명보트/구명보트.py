# 남은 사람 중 가장 무거운 사람과 가장 가벼운 사람의 합이 제한보다 무거우면,
# 가장 무거운 사람은 어차피 혼자 타야하므로 해당 경우를 먼저 고려한다.

def solution(people, limit):
       
    answer = 0
    
    people.sort()
    light = 0
    heavy = len(people) - 1
    
    while light <= heavy:
        if light == heavy:
            answer += 1
            break
        if people[light] + people[heavy] > limit:
            heavy -= 1
            answer += 1
        else:
            light += 1
            heavy -= 1
            answer += 1
    
    return answer