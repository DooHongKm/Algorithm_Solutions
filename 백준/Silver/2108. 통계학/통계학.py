import sys

n = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort()

temp = sum(numbers) / n
if temp >= 0:
  one = int(temp + 0.5)
else:
  one = int(-1 * temp + 0.5) * -1
  
two = numbers[n // 2]

four = max(numbers) - min(numbers)

dic = {}
for num in numbers:
  if num in dic:
    dic[num] += 1
  else:
    dic[num] = 1
max_ = max(dic.values())
max_num = []
for num in dic:
  if dic[num] == max_:
    max_num.append(num)
if len(max_num) == 1:
  three = max_num[0]
else:
  three = max_num[1]    
  
print(one)
print(two)
print(three)
print(four)    