'''
26.08.21
프로그래머스 - 도넛과 막대 그래프 / 구현

[포인트]
- DFS말고 생성정점을 시작 노드로 연결되어있는 노드를 방문
- 아웃 디그리가 == 0 -> 막대그래프++
- 아웃 디그리가 == 2 -> 8자 그래프++
- 시작 노드 == 끝 노드 -> 도넛 그래프++
'''

def get_max_node(edges):
    max_n1, max_n2 = -1, -1
    for n1, n2 in edges:
        if n1 > max_n1: max_n1 = n1
        if n2 > max_n2: max_n2 = n2
    return max_n1 if max_n1 > max_n2 else max_n2

def get_generated_node(g):
    n = len(g)
    degree = {i: [0, 0] for i in range(1, n+1)}
    # print(degree)
    
    for k, v in g.items():
        for i in v:
            degree[i][0] += 1
        degree[k][1] = len(v)
    
    for k, v in degree.items():
        if v[0] == 0 and v[1] >= 2:
            return k, degree
        
def solution(edges):
    answer = [0] * 4
    max_node = get_max_node(edges)
    g = {i: [] for i in range(1, max_node+1)}
    
    for n1, n2 in edges:
        g[n1].append(n2)
        
    generated_node, degree = get_generated_node(g)
    answer[0] = generated_node
    
    for sn in g[generated_node]:
        if degree[sn][1] == 0:
            answer[2] += 1; continue
        
        cur = g[sn][0]
        
        while True:
            if degree[cur][1] == 0:
                answer[2] += 1; break
            if degree[cur][1] == 2:
                answer[3] += 1; break
            if cur == sn:
                answer[1] += 1; break
            cur = g[cur][0]
            
    return answer
