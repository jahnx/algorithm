import math

def solution(n, m):
    answer = []
    GCD = math.gcd(n,m)
    LCM = n * m / GCD
    answer.append(GCD)
    answer.append(LCM)
     
    return answer