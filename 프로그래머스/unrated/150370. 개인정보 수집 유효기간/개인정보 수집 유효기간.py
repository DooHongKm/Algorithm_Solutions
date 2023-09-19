def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    year, month, day = map(int, today.split('.'))
    today = year * 12 * 28 + month * 28 + day
    print(today)
    for term in terms:
        left, right = term.split()
        term_dict[left] = int(right)
    for i, privacy in enumerate(privacies):
        left, right = privacy.split()
        y, m, d = map(int, left.split('.'))
        temp = y * 12 * 28 + m * 28 + d + term_dict[right] * 28
        print(temp)
        if today >= temp:
            answer.append(i + 1)
    return answer