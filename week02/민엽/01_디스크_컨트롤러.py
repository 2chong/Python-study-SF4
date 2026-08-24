'''
프로그래머스 - 디스크 컨트롤러
- https://school.programmers.co.kr/learn/courses/30/lessons/42627
- 힙 / 구현

[포인트]
- 비선점 SFJ 알고리즘 (프로세스 알고리즘)
  - 고정 순서로 처리 x , 동적 도착하는 후보 중 best 고르기 구조
- 힙 사용법을 알자 (heapq)
- 사실 힙 사용보다 구현이 더 어려웠음
'''

import heapq

def solution(jobs):
    jobs.sort(key=lambda x : x[0])
    current_time, HD, n = 0, 0, len(jobs)
    heap, result = [], []
    i = 0
    
    while len(result) < n:
        while i <= n-1 and jobs[i][0] <= current_time:
            request_time, excute_time = jobs[i][0], jobs[i][1]
            process = [excute_time, request_time, i]
            heapq.heappush(heap, process)
            i += 1
        
        if HD and HD[3] == current_time:
            result.append(HD)
            HD = 0
            
        if not HD and heap and heap[0][1] <= current_time:
            process = heapq.heappop(heap)
            process.append(current_time + process[0])
            HD = process
        
        current_time += 1
    
    hap = 0
    for r in result:
        hap += r[3]-r[1]
    return hap // len(result)
