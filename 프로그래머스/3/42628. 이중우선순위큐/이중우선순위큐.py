def solution(operations):
    
    queue = []
    
    for operation in operations:
        o, n = operation.split()
        n = int(n)
        if o == "I":
            queue.append(n)
            queue.sort()
        elif queue:
            if n == 1:
                queue.pop()
            else:
                queue.pop(0)
                
    if queue:
        return [max(queue), min(queue)]
    return [0, 0]
