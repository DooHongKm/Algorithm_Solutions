def solution(citations):

    max_ = max(citations)
    for i in range(max_, -1, -1):
        big = 0
        for c in citations:
            if c >= i:
                big += 1
        if big >= i:
            return i