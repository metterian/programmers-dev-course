#%%
# from the bottom up
def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1000000007
solution(4)
# %%
# Just count up (a naïve iterative solution)
def solution(n):
    a,b = 1,2
    for _ in range(n-1):
        a,b = b, a + b
    return a % 1000000007
solution(4)
# %%
# Memorization
def solution(n, computed={1: 1, 2:2}):
    if n not in computed:
        computed[n] = solution(n-1, computed) + solution(n-2, computed)
    return computed[n]
