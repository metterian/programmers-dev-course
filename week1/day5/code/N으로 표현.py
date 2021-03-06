#%%
N = 5
number = 12

# %%
from itertools import product

def solution(N, number):
    dp = [set() for _ in range(8+1)]

    for i in range(1, 8+1):
        dp[i].add(int(str(N)*i))
        for j in range(1, i):
            for op1, op2 in product(dp[j], dp[i-j]):
                dp[i].add(op1+op2)
                dp[i].add(op1-op2)
                dp[i].add(op1*op2)
                if op2 != 0:
                    dp[i].add(op1//op2)
        if number in dp[i]:
            return  (i)

    return -1


# %%
