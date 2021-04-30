#%%

signs = 	[[0,1,0],[0,0,1],[1,0,0]]
n = len(signs[0])
visited = [False * (n+1) for _ in range(n+1)]

def route(sign):
    result=[]
    for i, val in enumerate(sign, start=1):
        if val!=0:
            result.append(i)
    return result

from collections import deque

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return result




graph = {}
d = [[] for _ in range(n+1)]
for i, sign in enumerate(signs, start=1):
    graph[i] = route(sign)

for i, data in graph.items():
    visited = [False * (n+1) for _ in range(n+1)]
    result = []
    for start in data:
        d[i]+=(bfs(graph, visited, start))
#%%
answer = [[0]*n for _ in range(n+1)]
for i in range(1, n+1):
    for j in d[i]:
        if j !=0:
            answer[i][j-1] = 1

answer[1:]

# %%
