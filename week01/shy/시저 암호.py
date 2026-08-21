'''
[level 1] 시저 암호 - 12926
https://school.programmers.co.kr/learn/courses/30/lessons/12926
'''

def solution(s, n):
    answer = []
    
    for c in s:
        if c.isupper(): 
            shifted = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
            answer.append(shifted)
        elif c.islower():  
            shifted = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            answer.append(shifted)
        else: 
            answer.append(c)
            
    return "".join(answer)
