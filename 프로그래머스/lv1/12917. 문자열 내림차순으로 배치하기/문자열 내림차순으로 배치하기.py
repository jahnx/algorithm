def solution(s):

    tmp = list(map(lambda x: ord(x), s))
    tmp.sort(reverse=True)
    tmp = list(map(lambda x: chr(x), tmp))
    answer = ''
    for i in tmp:
        answer += i
    return answer