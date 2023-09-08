import sys
from collections import deque

while True :
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.': break
    
    stack = deque([])
    for char in sentence:
        if char == '(' or char == '[' :
            stack.append(char)
        elif char == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else : 
                stack.append(']')
        elif char == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')