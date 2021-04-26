#%%
from itertools import product, chain
monster = [4,9,5,8]
S1, S2, S3 = 2,3,3

# %%
encounter = 0
trial = 0
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            trial += 1
            if sum([i,j,k]) + 1 in monster:
                encounter+= 1

print(int((1-(encounter/trial)) * 1000))

# %%
# product를 이용한 풀이
encounter = 0
events = list(product(range(1, S1+1), range(1, S2+1), range(1,S3+1)))
trial = len(events)
for event in events:
    if sum(event) + 1 in monster:
        encounter += 1
print(int((1-(encounter/trial)) * 1000))

# %%
