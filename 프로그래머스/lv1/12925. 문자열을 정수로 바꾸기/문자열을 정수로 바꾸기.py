def solution(s):
    if s[0] == "-":
        s = s[1:]
        answer = -int(s)
        
    else:
        answer = int(s)
        
    return answer