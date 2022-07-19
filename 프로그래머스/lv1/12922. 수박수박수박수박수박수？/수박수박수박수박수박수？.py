def solution(n):
    answer = ''
    tmp = []
    for i in range(n):
        if i % 2 == 0:
            tmp.append("수")
        else:
            tmp.append("박")
            
    for i in tmp:
        answer += i
    return answer