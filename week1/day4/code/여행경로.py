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


    route.append(tickets[0][0])
    dfs(graph, visited, tickets[0])
    routes.append(route)

    return route
answer  = (solution(tickets))
answer

# %%
