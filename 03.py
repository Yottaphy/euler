def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True    

num = 600851475143
factor = 0
for i in range(2, num):
    if num%i == 0:
        if isPrime(int(num/i)):
            print(num/i)
            exit()