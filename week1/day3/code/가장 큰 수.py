#%%
numbers = [3, 30, 34, 5, 9]
numbers = list(map(str, numbers))


# %%
numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
# %%
int("".join(numbers))
# %%
