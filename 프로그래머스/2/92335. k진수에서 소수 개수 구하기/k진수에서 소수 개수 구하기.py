def solution(n, k):
    
    count = 0
    
    temp = ""
    while n > 0:
        temp = str(n % k) + temp
        n //= k
    numbers = temp.split('0')
    
    for number in numbers:
        if len(number) == 0 or number == '1':
            continue
        elif number == '2':
            count += 1
            continue
        num = int(number)
        temp = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                temp = False
                break
        if temp:
            count += 1
                
    return count