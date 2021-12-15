fibo = [1,2]
tot  = 2
flag = True
while flag:
    new = fibo[-2]+fibo[-1]
    fibo.append(new)
    if new >= 4E6:
        flag = False
        print(tot)
        exit()
    if new%2 == 0:
        tot += new