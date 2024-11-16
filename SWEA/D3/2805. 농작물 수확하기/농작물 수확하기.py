T = int(input())
for count in range(1, T + 1):

    N = int(input())
    values = [list(map(int, input())) for _ in range(N)]

    answer = 0
    center = N // 2
    for i in range(center + 1):
        temp = values[i]
        sum_ = sum(temp[center-i:center+i+1])
        answer += sum_
    values.reverse()
    for i in range(center):
        temp = values[i]
        sum_ = sum(temp[center-i:center+i+1])
        answer += sum_

    print(f"#{count} {answer}")