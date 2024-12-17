from math import gcd

def solution(arrayA, arrayB):
    
    result = 0
    
    arrayA.sort()
    arrayB.sort()
    
    gcdA = array_gcd(arrayA, arrayA[0])
    gcdB = array_gcd(arrayB, arrayB[0])
    while gcdA > 0:
        if check(arrayB, gcdA):
            result = max(result, gcdA)
            break
        gcdA = array_gcd(arrayA, gcdA - 1)
    while gcdB > 0:
        if check(arrayA, gcdB):
            result = max(result, gcdB)
            break
        gcdB = array_gcd(arrayB, gcdB - 1)
    
    return result
    
    
def array_gcd(arr, n):
    
    for num in arr:
        n = gcd(n, num)
    
    if n > 1:
        return n
    return 0
    
    
def check(arr, n):
    
    for num in arr:
        if num % n == 0:
            return False
    return True