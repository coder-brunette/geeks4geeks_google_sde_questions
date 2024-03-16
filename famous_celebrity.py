def famous_celebrity(M, n):
    i, j = 0, n-1
    candidate = -1
    print("i at first: ",i)
    print("j at first: ",j)
    while(i<j):
        if M[i][j] == 1:
            i += 1
            print("i:",i)
        else:
            j -= 1
            print("j:",j)
    candidate = i
    print(candidate)
    for k in range(n):
        if candidate != k:
            if M[candidate][k] == 1:
                return -1
    return candidate

n = 4
m = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]

print(famous_celebrity(m,n))
