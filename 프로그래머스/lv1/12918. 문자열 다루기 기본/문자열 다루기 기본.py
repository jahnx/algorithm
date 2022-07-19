def solution(s):
    if len(s)== 4 or len(s) == 6:
        if str.isdigit(s) == False:
            answer = False
        else:
            answer = True
    else:
        answer = False
    return answer