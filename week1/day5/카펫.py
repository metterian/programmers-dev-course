#%%
brown = 24
red = 24


if int(pow(red, 1/2)) == pow(red, 1/2):
    print (red+2, red+2)


# %%
reds = [r for r in range(1, red+1) if red % r == 0]

for row in reds[:len(reds)//2]:
    col = int(red/row)
    if 2*(col+row) + 4 == brown:
        if col >= row:
            print (col+2, row+2)




# %%
