'''
[level 1] 최대공약수와 최소공배수 - 12940
https://school.programmers.co.kr/learn/courses/30/lessons/12940
'''


def solution(n, m):
    a = max(n,m)
    b = min(n,m)   
    
    gcd = max(i for i in range(1, b+1) if a%i==0 and b%i==0)
    lcm = n*m//gcd
    
    return [gcd, lcm]
