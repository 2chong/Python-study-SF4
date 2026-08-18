'''
https://school.programmers.co.kr/learn/courses/30/lessons/468371?language=python3

문제 설명
어떤 도로에 차량 신호등이 n개 있습니다. 모든 신호등은 항상 초록불 → 노란불 → 빨간불 순서로 반복되며, 각 신호의 지속 시간은 신호등마다 다릅니다. 시간은 1초부터 시작하며, 각 신호등은 처음에는 초록불 상태로 시작합니다.

이 도로에서는 가끔 정전이 일어나는데, 모든 신호등이 모두 노란불이 되면 정전이 발생한다는 사실이 밝혀졌습니다.

예를 들어 신호등이 2개이고, 각 신호등의 주기가 다음과 같다고 가정해 보겠습니다.

신호등	초록불	노란불	빨간불
1번	2초	1초	2초
2번	5초	1초	1초
신호등-1.drawio.png

위 그림과 같이 13초에 처음으로 두 신호등이 모두 노란불이 됩니다.

신호등 n개의 신호 주기를 담은 2차원 정수 배열 signals가 매개변수로 주어집니다. 모든 신호등이 노란불이 되는 가장 빠른 시각(초)을 return 하도록 solution 함수를 완성해 주세요. 만약 모든 신호등이 노란불이 되는 경우가 존재하지 않는다면 -1을 return 해주세요.

제한사항
2 ≤ signals의 길이 = n ≤ 5
signals의 원소는 [G, Y, R] 형태의 길이가 3인 정수 배열입니다. 순서대로 초록불, 노란불, 빨간불의 지속 시간을 의미합니다.
1 ≤ G, Y, R ≤ 18
3 ≤ G + Y + R ≤ 20
테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹은 하나 이상의 하위 그룹으로 이루어져 있으며, 하위 그룹의 모든 테스트 케이스를 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.

그룹	총점	추가 제한 사항
#1	30%	신호등이 모두 노란불이 되는 시각이 20 이하인 정답이 존재합니다.
#2	30%	신호등이 모두 노란불이 되는 경우가 존재합니다.
#3	40%	추가 제한 사항 없음
입출력 예
signals	result
[[2, 1, 2], [5, 1, 1]]	13
[[2, 3, 2], [3, 1, 3], [2, 1, 1]]	11
[[3, 3, 3], [5, 4, 2], [2, 1, 2]]	193
[[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]	-1
입출력 예 설명
입출력 예 #1

문제 설명의 예시와 같습니다.

입출력 예 #2

신호등	초록불	노란불	빨간불
1번	2초	3초	2초
2번	3초	1초	3초
3번	2초	1초	1초
신호등-2.drawio.png

11초에 3개의 신호등이 모두 노란불이 됩니다.

입출력 예 #3

신호등	초록불	노란불	빨간불
1번	3초	3초	3초
2번	5초	4초	2초
3번	2초	1초	2초
193초에 3개의 신호등이 모두 노란불이 됩니다.

입출력 예 #4

모든 신호등이 노란불이 되는 경우가 존재하지 않으므로 -1을 return 해야 합니다.
'''

def solution(signals):
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a
    
    def lcm(a,b):
        return a*b/gcd(a,b)
    
    sum_signals = []
    for i in signals:
        sum_signals.append(sum(i))
        
    all_lcm = sum_signals[0]
    for i in sum_signals[1:]:
        all_lcm = lcm(all_lcm, i)
    print(all_lcm)
    all_lcm = int(all_lcm)
    
    count = 0
    result = 0
    for t in range(1, all_lcm+1):
        flag = False
        for x in signals:
            if x[0]+1<= t%sum(x)<x[0]+x[1]+1:
                count+=1
                if count == len(signals):
                    flag = True
        if flag == True:
            result = t
            break
        count = 0
    if flag == False:
        result = -1
    return result