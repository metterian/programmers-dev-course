#%%
# %%
arr = ["1", "-", "3", "+", "5", "-", "8"]
# %%
express = "".join(arr)
# %%
def divide(k, express):
    return [express[:k], express[k+1:]]




def calc(sol, i, express):
    if len(express) == 1:
        return express

    if len(express) ==3 :
        return eval(express)


    k = sol.pop(0) - i
    left, right = divide(k, express)
    result = eval(calc(sol, i+2, left)+express[k]+calc(sol, i+2, right))



# %%
