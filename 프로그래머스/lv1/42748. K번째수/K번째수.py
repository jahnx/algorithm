def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        tmp = array[start:end]
        tmp.sort()
        answer.append(tmp[commands[i][2] - 1])
        
    return answer