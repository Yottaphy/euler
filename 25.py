Fib = [1,1]
i = 2
while True:
    Fib.append(Fib[i-1] + Fib[i-2])
    if len(str(Fib[i]))==1000:
        print(i+1)
        break
    i+=1

