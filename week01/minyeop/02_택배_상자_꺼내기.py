'''
26.08.18
프로그래머스 택배 상자 꺼내기 / 배열(리스트), 구현
- https://school.programmers.co.kr/learn/courses/30/lessons/389478

[포인트]
1. 층 계산 로직
2. x_range 범위 (순방향, 역방향)
3. box 번호 넣으면서 num 값의 인덱스랑 i 끝 범위에서 break
4. num 값 인덱스에서 y축 +방향으로 몇개있는지 카운트
'''

def solution(n, w, num):
    floor = n//w+1 if n%w else n//w
    boxs = [[0 for _ in range(w)] for _ in range(floor)]
    cnt, i = 0, 1
    cy, cx = 0, 0
    
    for y in range(floor):
        x_range = range(w)
        if y % 2 != 0:
            x_range = range(w-1, -1, -1)
        
        for x in x_range:
            if num == i:
                cy, cx = y, x
            if i == n+1:
                break
            
            boxs[y][x] = i
            i += 1
    
    while cy < floor and boxs[cy][cx] != 0:
        cnt += 1
        cy += 1
        
    return cnt
