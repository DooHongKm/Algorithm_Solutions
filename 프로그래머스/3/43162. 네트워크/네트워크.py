def solution(n, computers):

    networks = []
    def isChecked(n):
        for network in networks:
            if n in network:
                return True
        return False
    
    for i in range(n):
        if isChecked(i):
            continue
        checked = []
        stack = [i]
        while stack:
            node = stack.pop()
            for j in range(n):
                if computers[j][node] == 1 and j not in checked:
                    stack.append(j)
                    checked.append(j)
        networks.append(checked)
        
    return len(networks)