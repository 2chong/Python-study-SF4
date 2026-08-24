'''
https://school.programmers.co.kr/learn/courses/30/lessons/340198

격자보고 바로 bfs인지 생각했는데, 그걸로 푸는 거보다 어차피 이 격자의 크기 제한이 50까지 밖에 안되서, 완전 탐색으로 하기로 함

1. 반복할 격자 범위 정하기
2. mat의 범위만큼 거기에 있는걸 set에 넣고 얘내가 -1로 될때 해당 mat 반환
3. for문 끝날 때까지 리턴 안되면 -1 리턴하기

문제 설명
지민이는 다양한 크기의 정사각형 모양 돗자리를 가지고 공원에 소풍을 나왔습니다. 
공원에는 이미 돗자리를 깔고 여가를 즐기는 사람들이 많아 지민이가 깔 수 있는 가장 큰 돗자리가 어떤 건지 확인하려 합니다. 
예를 들어 지민이가 가지고 있는 돗자리의 한 변 길이가 5, 3, 2 세 종류이고, 사람들이 다음과 같이 앉아 있다면 지민이가 깔 수 있는 가장 큰 돗자리는 3x3 크기입니다.

10.jpg

지민이가 가진 돗자리들의 한 변의 길이들이 담긴 정수 리스트 mats, 
현재 공원의 자리 배치도를 의미하는 2차원 문자열 리스트 park가 주어질 때 지민이가 깔 수 있는 가장 큰 돗자리의 한 변 길이를 return 하도록 solution 함수를 완성해 주세요. 
아무런 돗자리도 깔 수 없는 경우 -1을 return합니다.

'''

def solution(mats, park):
    mats = sorted(mats, reverse = True)
    for i in mats:
        extend = [row[:1-i] for row in park[:1-i]]
        row_range = len(park) - i + 1
        col_range = len(park[0]) - i + 1
        for row in range(row_range):
            for col in range(col_range):
                if park[row][col] == '-1':
                    s = set()
                    for r in range(row, row+i): 
                        for c in range(col, col+i):
                            s.add(park[r][c])
                    if s == {'-1'}:
                        return i
                        break
    return -1
