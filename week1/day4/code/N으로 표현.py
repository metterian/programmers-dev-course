#%%
N = 5
number = 12

# %%

# N이 1~ 9까지
dp = [set() for _ in range(1,9)]

# i개 만큼 만들수 있는 숫자 추가
for i ,x in enumerate(dp, start=1):
    x.add(int(str(N)*i))


for i in range(1, len(dp)):
    # i=1,
    for j in range(i):
        for op1 in dp[j]:
            for op2 in dp[i-j-1]:
                dp[i].add(op1+op2)
                dp[i].add(op1-op2)
                dp[i].add(op1*op2)
                if op2 != 0:
                    dp[i].add(op1//op2)

    if number in dp[i]:
        answer = i + 1
        break
else:
    answer = -1


print(answer)




# %%

# %%
