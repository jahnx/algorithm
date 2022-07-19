def solution(n):
    n = str(n)
    arr = []
    
    for i in n:
        arr.append(i)
    
    for i in arr:
        i = int(i)
        
    arr.sort(reverse = True)
    answer = ''
    for i in arr:
        answer += i
    return int(answer)