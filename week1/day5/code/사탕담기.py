#%%
m = 3000
weights = [500, 1500, 2500, 1000, 2000]


import sys
sys.setrecursionlimit(1500)

#%%
def dfs(x, i, weights,m):
    global answer
    total = sum([x*y for x,y in zip(weights, x)])
    # 종료 조건
    if  total == m:
        answer += 1
        return
    # 사탕 무게를 넘아가는 경우 더 이상 탐색을 하지 않는다.
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

# %%
from itertools import combinations

def solution(m, weights):
    answer = 0
    for i in range(1, len(weights)):
        sols = combinations(weights, i)
        for sol in sols:
            if sum(sol) == m:
                answer += 1
    return answer

# %%
from itertools import combinations
# 더 깔끔한 풀이
def solution(m, weights):
    answer = 0
    for i in range(1, len(weights)):
        answer += [sum(sol) for sol in combinations(weights, i)].count(m)
    return answer
