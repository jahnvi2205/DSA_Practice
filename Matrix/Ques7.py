def rotate90(mat):
    n = len(mat)

    # Perform Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Reverse each row
    for row in mat:
        row.reverse()