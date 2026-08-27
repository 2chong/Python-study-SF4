'''
프로그래머스 - 소수 찾기 / 완전탐색, 백트래킹
- https://school.programmers.co.kr/learn/courses/30/lessons/42839
- 코테에 자주 나오는 완전탐색 문제
- O(N!)이지만 문제 조건 상 N이 1~7이라 완탐으로 충분히 가능!!
- 문제 패턴을 외울 필요가 있음
- 왜 난 이렇게 생각 못했지 그런 생각 절대 x -> 그냥 이런 아이디어가 있고 아이디어를 잘 가져가서 쓰면 그만임
- 그리고 이런 완탐류 문제의 itertools 라이브러리가 있는데
  - 이것도 잘 알아두면 좋을꺼임 -> 코드가 간결해짐
  - 일단 라이브러리를 쭉 쓰는것보단 공부용으로는 먼저 코드를 직접 작성하는게 좋아보임!!
  - 맨 밑 주석에 itertools 라이브러리를 활용한 get_perm 함수도 추가해놨음
'''

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def get_permutaion(numbers):
    n = len(numbers)
    v = [0] * n
    perm = set()
    
    def DFS(current_str):
        if len(current_str) == n:
            perm.add(int(current_str))
            return
        for i, s in enumerate(numbers):
            if v[i] == 0:
                perm.add(int(current_str+s))
                v[i] = 1
                DFS(current_str+s)
                v[i] = 0
                
    DFS('')
    return perm

def solution(numbers):
    perm = get_permutaion(numbers)
    cnt = 0
    
    for p in perm:
        if is_prime(p): cnt += 1
    
    return cnt
  
'''
from itertools import permutations

def get_perm(numbers):
    n = len(numbers)
    perm = set()
    for r in range(1, n+1):
        for p in permutations(numbers, r):
            perm.add(int(''.join(p)))
    return perm
'''
