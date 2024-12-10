def solution(numbers):

    answer = ""
    
    temp = [0 for _ in range(len(numbers))]
    for i in range(len(numbers)):
        number = str(numbers[i])
        number = (number * 4)[:4]
        temp[i] = (number, i)
        
    temp.sort(reverse=True, key=lambda x: x[0])
    for t, i in temp:
        answer += str(numbers[i])
        
    if answer[0] == "0":
        return "0"
    return answer