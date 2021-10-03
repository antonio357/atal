def printMatrix(m):
    print()
    for i in m: print(i)

def recursive():
    pass

def memoized():
    pass

def dynamicPrograming(s, n, w):
    m = list()
    for r in range(w + 1):
        m.append(list())
        for c in range(n + 1):
            if r == 0 or c == 0: m[r].append(0)
            else: m[r].append('-')
    printMatrix(m)

    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if s[i].peso > w: m[w][i] = m[w][i - 1]
            else: m[w][i] = max(m[w - s[i].peso][i - 1] + s[i].valor, m[w][i - 1])

    printMatrix(m)
    return m[w][n]

class item():
    def __init__(self, peso, valor):
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