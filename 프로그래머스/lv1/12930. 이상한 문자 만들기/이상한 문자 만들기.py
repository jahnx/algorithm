def solution(s):
    answer = ''
    words_list = s.split(' ')
    
    for word in words_list:
        for j in range(len(word)):
            if j % 2 == 0:
                answer += word[j].upper()
            else:
                answer += word[j].lower()
        answer += ' '
        
    return answer[:-1]
