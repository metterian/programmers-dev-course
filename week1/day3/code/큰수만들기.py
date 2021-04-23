#%%
number = "4177252841"
k = 4
def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected = collected + list(number[i:])
            break

        collected.append(num)

    if k > 0:
        collected = number[:-k]
    return "".join(collected)

solution("98765", 3)
# %%
