#%%
number = "4177252841"
k = 4
def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        # collected에 원소가 있어야 peek을 할 수 있다. 이전에 들어간게 지금 것 보다
        # 작으면 이전(왼쪽)에 숫자를 빼야 한다, 단, k가 존재 할 때 까지
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
