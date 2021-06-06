longest = 0
best    = 0
for i in range(2,1000001):
    chain = [i]
    j = i
    while not j==1:
        if j%2 == 0:
            j = j/2
        else:
            j = 3*j + 1
        chain.append(j)
    if len(chain) > longest:
        longest = len(chain)
        best    = i
print(best)   


