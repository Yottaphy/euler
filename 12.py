def Triangle(n):
    tot = 0
    for i in range(n+1): tot+=i
    return tot

listDiv =[]
n = 1
while len(listDiv) <= 500:
    num = Triangle(n)
    listDiv = []
    for i in range(1,num+1):
        if num%i == 0:
            if i in listDiv: break
            listDiv.append(i)
            listDiv.append(num/i)
    n+=1
print(num)