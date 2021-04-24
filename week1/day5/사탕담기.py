#%%

m = 3000
weights = [500, 1500, 2500, 1000, 2000]


import sys
sys.setrecursionlimit(1500)


def dfs(x, i, weights,m):
    global answer
    total = sum([x*y for x,y in zip(weights, x)])
    if  total == m:
        answer += 1
        return

    if i >= len(weights) or total > m:
        return

    for j in range(i, len(weights)):
        x[j] = 1
        dfs(x, j+1, weights,m)
        x[j] = 0

answer = 0
def solution(m, weights):
    global x, answer
    x = [0] * len(weights)

    dfs(x, 0, weights,m)


    return answer
