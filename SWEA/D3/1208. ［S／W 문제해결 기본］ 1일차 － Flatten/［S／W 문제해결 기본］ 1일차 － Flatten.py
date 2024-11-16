for count in range(1, 11):

    high = 0
    low = 0

    n = int(input())
    numbers = list(map(int, input().split()))

    temp = [0 for _ in range(101)]
    for number in numbers:
        for i in range(number + 1):
            temp[i] += 1

    add = n
    sub = n
    avg = sum(temp) // 100

    for i in range(avg + 2):
        t = temp[i]
        if t < 100:
            add -= 100 - t
            if add == 0:
                low = i
                break
            if add < 0:
                low = i - 1
                break
    for i in range(100, avg, -1):
        t = temp[i]
        if t > 0:
            sub -= t
            if sub <= 0:
                high = i
                break

    print(f"#{count} {high-low}")

