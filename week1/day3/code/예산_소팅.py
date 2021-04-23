#%%
d = [1,3,2,5,4]
budget = 9
# %%
d.sort()
# %%
result = 0

for i, price in enumerate(d):
    if result + i > budget:
        break
    result += price

print(i+1)
# %%
