def matrix_addition(a, b):
    res = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j] = a[i][j] + b[i][j]

    printMatrix(res)
    return res

def matrix_subraction(a, b):
    res = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j] = a[i][j] - b[i][j]

    printMatrix(res)
    return res

def printMatrix(m):
    print("="*20)
    print("Printing the matrix: ")
    print("="*20)
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end = " ")
        print()