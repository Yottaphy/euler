def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

largest = 0
for i in range(999,100, -1):
    for j in range(i, 100, -1):
        if isPalindrome(i*j) and i*j > largest:
            largest = i*j

print(largest)