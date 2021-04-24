#%%
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# %%


route = []
def dfs(graph, visited, start):
    dept, arrive = start
    visited[dept+arrive] = True
    route.append(arrive)

    for next_arrive in sorted(graph[arrive]):
        if not visited[arrive+next_arrive]:
            dfs(graph, visited, [arrive,next_arrive])


def solution(tickets):
    global route
    routes = []
    graph = {}
    for dept, arrive in tickets:
        graph[dept] = []
        graph[arrive] = []
    for dept, arrive in tickets:
        graph[dept].append(arrive)

    visited = {}
    for dept, arrive in tickets:
        visited[dept+arrive] = False

    route.append('ICN')
    for start in sorted(graph["ICN"]):
        dfs(graph, visited, ['ICN', start])
        routes.append(route)
        route = []

    return max(routes, key=len)
answer  = (solution(tickets))
answer

# %%
def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) ==0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]

solution(tickets)
# %%
