def printCommonElements(mat):
    mp = dict()
    for j in range(N):
        mp[(mat[0][j])] = 1

    for i in range(1, M):
        for j in range(N):
            if (mat[i][j] in mp.keys() and mp[(mat[i][j])] == i):
                mp[(mat[i][j])] = i + 1
                if i == M - 1:
                    print(mat[i][j], end = " ")
            
