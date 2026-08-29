'''
프로그래머스 - lv 2. N-Queen / 완전탐색, 백트래킹
- 왜 2레벨 문제인지 모르겠다 <- 쉬운 3렙보다 어려운거같음 아직 안익숙해서 그런거같기도
  - 인덱스 에러랑 재귀때매 머리털 다 빠지는줄
- 문제 패턴 찾는데 꽤 시간이 걸렸다
- 문제점 및 해결:
  - 좌우 대각선 로직에서 조건을 잘 보고 하자
    - i, j를 조건에 맞게 먼저 할당하고 while문을 보게하면 인덱스 터질 일 x
    
  - 여러 퀸의 공격 범위가 겹칠때 백트래킹을 잘못하면 아직 다른 퀸이 공격 중인 칸까지 같이 풀려버림
    - 공격 받는 횟수(delta)를 세는 방식으로 바꿨음
  
  - total값 리턴하는건 아직 좀 헷갈림
    - cnt를 바깥 변수로 두고 DFS 돌리면 nonlocal 필요해서 복잡
    - 대신에 DFS가 total로 직접 리턴하고 부모가 그값을 total += DFS(...)로 모으는게 좀 더 깔끔
    - 개수 세는 백트래킹 문제 나오면 상기하기
'''

def solution(n):    
    def get_marking_board(y, x, marking):
        delta = 1 if marking else -1
        
        for i in range(y): board[i][x] += delta # 상
        for i in range(y+1, n): board[i][x] += delta # 하
        for i in range(x): board[y][i] += delta # 좌
        for i in range(x+1, n): board[y][i] += delta # 우
        
        i, j = y-1, x-1
        while i >= 0 and j >= 0: # 좌상 대각
            board[i][j] += delta
            i -= 1; j -= 1;
        i, j = y-1, x+1
        while i >= 0 and j < n: # 우상 대각
            board[i][j] += delta
            i -= 1; j += 1
        i, j = y+1, x-1
        while i < n and j >= 0: # 좌하 대각
            board[i][j] += delta
            i += 1; j -= 1
        i, j = y+1, x+1
        while i < n and j < n: # 우하 대각
            board[i][j] += delta
            i += 1; j += 1
        
        
    def DFS(y, x):
        if y == n-1: return 1
        
        total = 0
        for nx, value in enumerate(board[y+1]):
            if value == 0:
                board[y+1][nx] = 1
                get_marking_board(y+1, nx, True)
                total += DFS(y+1, nx)
                board[y+1][nx] = 0
                get_marking_board(y+1, nx, False)
        
        return total
    
    
    m = (n//2)-1 if n%2 == 0 else n//2
    result = []
    
    for x in range(m+1):
        board = [[0 for _ in range(n)] for _ in range(n)]
        board[0][x] = 1
        get_marking_board(0, x, True)
        total = DFS(0, x)
        result.append(total)
        
    print(result)
    return 2*sum(result) if n%2 == 0 else 2*sum(result[:m]) + result[m]
