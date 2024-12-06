from collections import deque

def solution(begin, target, words):

    def check(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        return count == 1
    
    answer = float("inf")
    queue = deque([(0, begin, set())])
    while queue:
        idx, cur, used = queue.popleft()
        if cur == target:
            return idx
        for word in words:
            if check(cur, word) and word not in used:
                
                queue.append((idx+1, word, used|{word}))
                
    return 0
    
    