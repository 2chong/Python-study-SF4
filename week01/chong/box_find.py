'''
https://school.programmers.co.kr/learn/courses/30/lessons/389478

1. 마지막 줄에서 index별 상자 유무 확인
2. 택배상자의 번호가 있는 곳이 짝수줄인지 홀수줄인지 확인
  
1 ~ n의 번호가 있는 택배 상자가 창고에 있습니다. 당신은 택배 상자들을 다음과 같이 정리했습니다.

왼쪽에서 오른쪽으로 가면서 1번 상자부터 번호 순서대로 택배 상자를 한 개씩 놓습니다. 가로로 택배 상자를 w개 놓았다면 이번에는 오른쪽에서 왼쪽으로 가면서 그 위층에 택배 상자를 한 개씩 놓습니다. 그 층에 상자를 w개 놓아 가장 왼쪽으로 돌아왔다면 또다시 왼쪽에서 오른쪽으로 가면서 그 위층에 상자를 놓습니다. 이러한 방식으로 n개의 택배 상자를 모두 놓을 때까지 한 층에 w개씩 상자를 쌓습니다.

ex1-1.png

위 그림은 w = 6일 때 택배 상자 22개를 쌓은 예시입니다.
다음 날 손님은 자신의 택배를 찾으러 창고에 왔습니다. 당신은 손님이 자신의 택배 상자 번호를 말하면 해당 택배 상자를 꺼내줍니다. 택배 상자 A를 꺼내려면 먼저 A 위에 있는 다른 모든 상자를 꺼내야 A를 꺼낼 수 있습니다. 예를 들어, 위 그림에서 8번 상자를 꺼내려면 먼저 20번, 17번 상자를 꺼내야 합니다.

당신은 꺼내려는 상자 번호가 주어졌을 때, 꺼내려는 상자를 포함해 총 몇 개의 택배 상자를 꺼내야 하는지 알고 싶습니다.

창고에 있는 택배 상자의 개수를 나타내는 정수 n, 가로로 놓는 상자의 개수를 나타내는 정수 w와 꺼내려는 택배 상자의 번호를 나타내는 정수 num이 매개변수로 주어집니다. 이때, 꺼내야 하는 상자의 총개수를 return 하도록 solution 함수를 완성해 주세요.
'''

def solution(n, w, num):
    h = n//w
    if h % 2 == 0:
        isin = [i < n%w for i in range(w)]
        print(isin)
    else:
        isin = [i >= w-n%w for i in range(w)]
        print(isin)
    
    if num%w == 0:
        target_h = num//w
        if target_h % 2 == 0:
            target_w = 0
        else:
            target_w = w-1
    else:
        target_h = num//w + 1
        if target_h % 2 == 0:       
            target_w = w-num%w
        else:
            target_w = num%w - 1
            
    if h - target_h == 0:
        answer = 1
    else:
        boxes1 = h - target_h + 1
        if isin[target_w]:
            answer = boxes1 + 1
        else:
            answer = boxes1
    return answer
