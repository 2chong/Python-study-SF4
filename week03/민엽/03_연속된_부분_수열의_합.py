'''
프로그래머스 - lv 2. 연속된 부분 수열의 합 / 부분합, 투 포인터
- https://school.programmers.co.kr/learn/courses/30/lessons/178870
- prefix_sum 앞에 0을 붙이는 패턴
- sort 메소드 key 파라미터의 사용법을 활용하자
'''

def solution(sequence, k):
    i, j, n = 0, 1, len(sequence)
    prefix_sum, result = [0]*(n+1), []
    
    for idx in range(n):
        prefix_sum[idx+1] = prefix_sum[idx] + sequence[idx]
        
    # print(prefix_sum)
    
    while j <= n:
        diff = prefix_sum[j] - prefix_sum[i]
        if diff < k: j += 1
        elif diff > k: i += 1
        else:
            result.append([i, j-1])
            i += 1
    
    result.sort(key=lambda x : (x[1]-x[0], x[0]))
    
    # print(result)
    
    return result[0]
