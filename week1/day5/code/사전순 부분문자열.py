#%%
s = 'yxyc'
# %%

def solution(s):
    stack = []
    for char in s:
        while stack and stack[-1] < char :
            stack.pop()
        stack.append(char)
    return ("".join(stack))

solution(s)
# %%

# %%
