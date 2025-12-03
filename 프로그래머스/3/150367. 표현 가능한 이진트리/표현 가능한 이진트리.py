def determine(number):

    number_bin = bin(number)[2:]
    count = len(number_bin)

    depth = 1
    while count > pow(2, depth) - 1:
        depth += 1

    length = pow(2, depth) - 1
    number = "0" * (length - count) + number_bin

    stack = [(0, length - 1, True)]
    
    while stack:
        left, right, first = stack.pop()
        mid = (left + right) // 2

        if first and number[mid] == "0":
            return 0
        if left >= right:
            continue

        left_mid = (left + mid - 1) // 2
        right_mid = (mid + 1 + right) // 2
        if number[mid] == "0":
            if number[left_mid] == "1" or number[right_mid] == "1":
                return 0
        
        stack.append((left, mid - 1, False))
        stack.append((mid + 1, right, False))

    return 1


def solution(numbers):

    return [determine(number) for number in numbers]