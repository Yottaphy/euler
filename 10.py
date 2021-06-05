from eulerfuncs import isPrime
total =0
for i in range(1, int(2E6)):
    total += i if isPrime(i) else 0

print(total)