#%%
strs =["ba","na","n","a"]
t = 'banana'


# %%

def dfs(x, i, strs,t):
    global answer,flag
    if i > len(strs)-1:
        return
    word = "".join([char*sol for char, sol in zip(strs, x) if sol!=0])
    # 종료 조건
    if  word == t:
        answer = min(answer, sum(x))
        flag = True
        return
    # 사탕 무게를 넘아가는 경우 더 이상 탐색을 하지 않는다.
    for ele, t_ele in zip(word, t):
        if ele !=t_ele:
            return

    for j in range(len(strs)):
        x[j] += 1
        dfs(x, j+1, strs,t)
        x[j] -= 1
        if flag: return
flag = False
answer = 1e9
def solution(strs, t):
    global x, answer, flag
    x = [0] * len(strs)

    dfs(x, 0, strs,t)
    return answer
solution(strs, t)
# %%
