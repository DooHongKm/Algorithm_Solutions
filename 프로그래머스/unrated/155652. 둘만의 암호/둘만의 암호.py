from collections import deque

def solution(s, skip, index):
    result = []
    alpha_dict = {}
    alphas = deque("abcdefghijklmnopqrstuvwxyz")
    for a in skip:
        alphas.remove(a)
    for i in range(len(alphas)):
        alpha_dict[alphas[i]] = i
    for a in s:
        temp = alpha_dict[a]
        result.append(alphas[(temp + index) % len(alphas)])
    return "".join(result)