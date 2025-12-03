def solution(cookie):

    result = 0

    for i in range(1, len(cookie)):
        first = sum(cookie[:i])
        second = sum(cookie[i:])

        fIdx = 0
        sIdx = len(cookie) - 1

        def calc_first():
            nonlocal first, fIdx
            first -= cookie[fIdx]
            fIdx += 1

        def calc_second():
            nonlocal second, sIdx
            second -= cookie[sIdx]
            sIdx -= 1

        while fIdx < i and sIdx >= i:
            if first == second:
                result = max(result, first)
                break
            if first > second:
                calc_first()
            else:
                calc_second()

    return result