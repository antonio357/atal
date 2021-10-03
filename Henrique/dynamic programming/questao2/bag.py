def printMatrix(m):
    print()
    for i in m: print(i)

def recursive():
    pass

def memoized():
    pass

def dynamicPrograming(s, n, w):
    matrix = list()
    for r in range(w + 1):
        matrix.append(list())
        for c in range(n + 1):
            if r == 0 or c == 0: matrix[r].append(0)
            else: matrix[r].append('-')
    printMatrix(matrix)

    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if s[i].peso > w: matrix[w][i] = matrix[w][i - 1]
            else: matrix[w][i] = max(matrix[w - s[i].peso][i - 1] + s[i].valor, matrix[w][i - 1])

    printMatrix(matrix)
    return matrix[w][n]

class item():
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

s = {
    1: item(6, 30),
    2: item(3, 14),
    3: item(4, 16),
    4: item(2, 9)
}
n, w = 4, 10

print(dynamicPrograming(s, n, w))