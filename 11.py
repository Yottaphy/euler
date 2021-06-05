def sumS(matrix, i, j):
    tot = 1
    for a in range(0,4):
        tot *= matrix[i+a][j]
    return tot

def sumN(matrix, i, j):
    tot = 1
    for a in range(0,4):
        tot *= matrix[i-a][j]
    return tot

def sumE(matrix, i, j):
    tot = 1
    for a in range(0,4):
        tot *= matrix[i][j+a]
    return tot

def sumW(matrix, i, j):
    tot = 1
    for a in range(0,4):
        tot *= matrix[i][j-a]
    return tot

def sumSW(matrix,i,j):
    tot = 1
    for a in range(0,4):   
        tot *= matrix[i+a][j-a]
    return tot

def sumSE(matrix,i,j):
    tot = 1
    for a in range(0,4):   
        tot *= matrix[i+a][j+a]
    return tot

def sumNW(matrix,i,j):
    tot = 1
    for a in range(0,4):   
        tot *= matrix[i-a][j-a]
    return tot

def sumNE(matrix,i,j):
    tot = 1
    for a in range(0,4):   
        tot *= matrix[i-a][j+a]
    return tot

file = open('11_nums.txt')
matrix = [[int(num) for num in line.split(',')] for line in file]

totmax = 0
for i in range(0,20):
    for j in range(0,20):
        com = []
        if i <= 16:
            com.append(sumS(matrix,i,j))
            if j <= 16: com.append(sumSE(matrix,i,j))
        if i >= 3: 
            com.append(sumN(matrix,i,j))
            if j >= 3: com.append(sumNW(matrix,i,j))
        if j <= 16:
            com.append(sumE(matrix,i,j))
            if i >= 3: com.append(sumNE(matrix,i,j))
        if j >= 3: 
            com.append(sumW(matrix,i,j))
            if i <= 16: com.append(sumSW(matrix,i,j))
        if max(com) > totmax: totmax = max(com)
        
print(totmax)
