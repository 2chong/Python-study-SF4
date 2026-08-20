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
            return k
        
def solution(edges):
    answer = [0] * 4
    max_node = get_max_node(edges)
    g = {i: [] for i in range(1, max_node+1)}
    
    for n1, n2 in edges:
        g[n1].append(n2)
        
    generated_node = get_generated_node(g)
    answer[0] = generated_node
    visited = [0] * (max_node+1)
    
    def DFS(start_node):
        nonlocal node_cnt, edge_cnt
        
        if visited[start_node] == 1:
            return
        
        node_cnt += 1
        edge_cnt += len(g[start_node])
        visited[start_node] = 1
        
        # print(start_node, node_cnt, edge_cnt)
        
        for i in g[start_node]:
            if visited[i] == 0:
                DFS(i)
    
    for k, v in g.items():
        if k == generated_node or visited[k] == 1:
            continue
            
        node_cnt, edge_cnt = 0, 0
        DFS(k)
        
        if node_cnt - edge_cnt == 0: answer[1] += 1
        elif node_cnt - edge_cnt == 1: answer[2] += 1
        else: answer[3] += 1
    
    return answer
