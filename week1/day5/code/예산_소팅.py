#%%
from itertools import combinations
d = [1,3,2,5,4]
budget = 9


answer = 0
d.sort()
for i in range(1, len(d)+1):
    for sols in combinations(d, i):
        if sum(sols) <= budget:
            answer = i
            break
        else:
            break
print(answer)
# %%
