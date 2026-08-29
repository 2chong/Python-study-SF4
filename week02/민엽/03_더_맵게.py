'''
프로그래머스 - lv 2. 더 맵게 / 힙, 구현

- 문제가 쉬운편이면 최적화를 고려하자
  - 이 문제는 구현은 쉽지만 최적화(복잡도)를 안하면 통과를 못함
  - 그래서 힙이라는 자료구조를 써야함

- 파이썬은 최소 힙만 제공 -> 최대힙을 하려면 약간의 꼼수가 필요
- 힙의 개념과 사용법을 알자 (heapq 라이브러리)
  - 힙을 직접 구현할 일은 거의 없지만 시간이 남는다면 AI를 활용하여 한번 만들어보자
  - 이해하는데 큰 도움이 될듯하다
- 밑에 코드는 시간복잡도가 터지는 코드: 시간복잡도를 계산해보자!
  - 먼저 제한사항을 보고 어떤식으로 해야겠다라는 틀을 먼저 잡는것이 중요하다 <- 근데 난 잘 못함 ㅠㅠ
  - 예를 들어 N이 1~20이라면 완전탐색을 해볼수있을것이고 뭐 이런거
- 간단한 힙 사용법
  - hq.heapify(list): 리스트를 힙으로, O(N)
  - hq.heappush(list, element): 힙에 원소 추가, O(logN)
  - hq.heappop(list): 힙에서 가장 최솟값 삭제, O(logN)
  - heapify 해도 내부적으로는 list로 동작해서 인덱싱으로 접근이 가능함
'''

import heapq as hq

def solution(scoville, K):
    cnt = 0
    hq.heapify(scoville)
    
    while len(scoville) != 1 and scoville[0] < K:
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + 2*second)
        cnt += 1
        
    if scoville[0] >= K:
        return cnt
    return -1

'''
def is_all_check(scoville, K):
    for s in scoville:
        if s < K:
            return False
    return True

def solution(scoville, K):
    cnt = 0
    
    while len(scoville) != 1:
        if is_all_check(scoville, K):
            return cnt
        
        first = min(scoville)
        scoville.remove(first)
        
        second = min(scoville)
        scoville.remove(second)
        
        scoville.append(first + 2*second)
        
        cnt += 1
    
    if scoville[0] >= K:
        return cnt
    
    return -1
'''
