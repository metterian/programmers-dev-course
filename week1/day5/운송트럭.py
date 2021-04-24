#%%
max_weight = 200
specs = [["toy","70"], ["snack", "200"]]
names = ["toy", "snack", "toy"]
# %%

def solution(max_weight, specs, names):
    spec = {}
    for name, weight in specs:
        spec[name] = int(weight)


    answer = 1
    truck = 0

    for name in names:
        if truck + spec[name] > max_weight:
            answer += 1
            truck = spec[name]
        else:
            truck += spec[name]


    return (answer)

solution(max_weight, specs, names)
# %%
