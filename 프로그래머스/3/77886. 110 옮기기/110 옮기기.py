def transform(num):

    if "110" not in num:
        return num

    count = 0
    stack = [num[0]]
    for n in num[1:]:
        if len(stack) >= 2 and stack[-2] == stack[-1] == "1" and n == "0":
            count += 1
            for _ in range(2):
                stack.pop()
        else:
            stack.append(n)

    temp = "110" * count
    remain = "".join(stack)    

    if remain == "":
        return temp

    if "111" in remain:
        idx = remain.find("111")
        return remain[:idx] + temp + remain[idx:]

    if remain[-2:] == "11":
        return remain[:-2] + temp + remain[-2:]

    if remain[-1] == "1":
        return remain[:-1] + temp + remain[-1:]

    return remain + temp


def solution(s):

    return [transform(num) for num in s]