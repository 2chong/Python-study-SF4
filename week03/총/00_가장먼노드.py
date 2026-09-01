'''
https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3

1. graph 만들어서 몇번노드가 몇번노드와 연결되어 있는지 알 수 있게. 
2. BFS쓰는데, 그 전에 Distance 빈 배열 만들어놓고 하나씩 더해가면서 +1 해주기
3. 그리고 각 노드의 Distance를 찾았으면 굿

n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.


'''


from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n + 1)
    distance[1] = 0
    queue = deque([1])
    
    while queue:
        cur = queue.popleft()
        for next_node in graph[cur]:
            if distance[next_node] == -1:
                distance[next_node] = distance[cur] + 1
                queue.append(next_node)
    
    max_distance = max(distance[1:])
    return distance[1:].count(max_distance)
