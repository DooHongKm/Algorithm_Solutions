from collections import deque

def solution(people, limit):

    count = 0
    
    people = deque(sorted(people))
    while len(people) > 0:
        if len(people) == 1:
            count += 1
            break
        else:
            if people[0] + people[-1] > limit:
                people.pop()
            else:
                people.pop()
                people.popleft()
            count += 1
            
    return count