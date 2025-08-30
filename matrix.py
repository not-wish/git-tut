def matrix_addition(a, b):
    res = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j] = a[i][j] + b[i][j]

    return res

def matrix_subraction(a, b):
    res = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j] = a[i][j] - b[i][j]

    return res