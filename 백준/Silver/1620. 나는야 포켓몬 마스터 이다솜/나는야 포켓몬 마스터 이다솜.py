import sys

n, m = map(int, sys.stdin.readline().split())

pokemon_dict = {}
for i in range(n):
  temp = sys.stdin.readline().rstrip()
  pokemon_dict[i+1] = temp
  pokemon_dict[temp] = i + 1
  
for i in range(m):
  question = sys.stdin.readline().rstrip()
  if question[0].isalpha():
    print(pokemon_dict[question])
  else:
    print(pokemon_dict[int(question)])