def solution(s):

    result = 0
    stack = [(1, s - 1, s)]

    while stack:
        cur, lparen, rparen = stack.pop()
        if cur == lparen == rparen == 0:
            result += 1
            continue
        if lparen > 0:
            stack.append((cur + 1, lparen - 1, rparen))
        if cur > 0 and rparen > 0:
            stack.append((cur - 1, lparen, rparen - 1))

    return result