for _ in range(1, 11):

    count = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    ladder.reverse()
    start = ladder[0].index(2)

    def check(x, y):
        if start > 0 and ladder[y][x-1] == 1:
            return "l"
        if start < 99 and ladder[y][x+1] == 1:
            return "r"
        return "b"

    def left(x, y):
        index = 1
        while True:
            if x - index >= 0 and ladder[y][x - index] == 1:
                index += 1
            else:
                break
        return x - index + 1

    def right(x, y):
        index = 1
        while True:
            if x + index < 100 and ladder[y][x + index] == 1:
                index += 1
            else:
                break
        return x + index - 1

    for i in range(1, 101):
        if i == 100:
            break
        temp = check(start, i)
        if temp == "l":
            start = left(start, i)
            continue
        if temp == "r":
            start = right(start, i)
            continue

    print(f"#{count} {start}")