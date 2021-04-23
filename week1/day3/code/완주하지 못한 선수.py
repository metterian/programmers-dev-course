# %%
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
#%%
from collections import defaultdict
def solution(participant, completion):
    d = defaultdict()
    for x in participant:
        d[x] = d.get(x, 0) + 1

    for x in completion:
        d[x] -= 1

    dnf = [k for k,v in d.items() if v > 0]
    answer = dnf[0]
    return answer


solution(participant, completion)
# %%
