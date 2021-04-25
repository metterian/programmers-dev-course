#%%
# %%
numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = list(sorted(numbers, key=lambda x: (x*4)[:4], reverse=True ))
    return str(int("".join(numbers)))

# %%

# %%
