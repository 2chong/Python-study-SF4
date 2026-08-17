'''
프로그래머스 문자열/투 포인터 문제
문자열 압축
https://school.programmers.co.kr/learn/courses/30/lessons/60057

[포인트]
- 파이썬 슬라이싱은 범위 넘어가도 알아서 있는데까지만 잘라줌 <- 처음 앎
- for-else문: for문에서 한번도 실행안하면 else문 실행함 <- 까먹고 있었음
'''

def encoding(k, s):
    sl = []
    n = len(s)
    
    for i in range(0, n, k):
        sl.append(s[i:i+k])
    
    # print(sl)
    
    rs = ''
    m = len(sl)
    i = 0
    
    while i <= m-1:
        c1 = sl[i]
        cnt = 1
        for j in range(i+1, m):
            c2 = sl[j]
            if c1 == c2: 
                cnt += 1
                i += 1
            else: 
                i = j
                break
        
        else:
            i += 1
            
        if cnt == 1: rs += c1
        else: rs += str(cnt)+c1
    
    return rs


def solution(s):
    if len(s) == 1: return 1

    min_cnt = float('inf')
    n = len(s)
    
    for i in range((n//2)):
        k = i+1
        encoded_s = encoding(k, s)
        # print(k, encoded_s)
        
        if min_cnt > len(encoded_s):
            min_cnt = len(encoded_s)
    
    return min_cnt
