def printMatrix(m):
    print()
    for i in m: print(i)

def initMatrix(m, n, w):
    for r in range(w + 1):
        m.append(list())
        for c in range(n + 1):
            m[r].append(0)

# int knapsackRec(int[] w, int[] v, int n, int W) {
#     if (n <= 0) {
#         return 0;
#     } else if (w[n - 1] > W) {
#         return knapsackRec(w, v, n - 1, W);
#     } else {
#         return Math.max(knapsackRec(w, v, n - 1, W), v[n - 1]
#           + knapsackRec(w, v, n - 1, W - w[n - 1]));
#     }
# }

def f(w, v, n, W):
    if n <= 0: return 0
    elif w[n - 1] > W: return f(w, v, n - 1, W)
    return max(f(w, v, n - 1, W), v[n - 1] + f(w, v, n - 1, W - w[n - 1]))

# def recursive(s, n, w):
#     if n == 0: return 0
#     elif s[n - 1].peso > s[w].peso: return recursive(s, n - 1, w)
#     return max(recursive(s, n - 1, w), s[n - 1].valor + recursive(s, n - 1, w - 1))

def memoized():
    pass

def dynamicPrograming(s, n, w):
    m = list()
    initMatrix(m, n, w)
    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if s[i].peso > w: m[w][i] = m[w][i - 1]
            else: m[w][i] = max(m[w - s[i].peso][i - 1] + s[i].valor, m[w][i - 1])
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
# print(recursive(s, n, w))
w1, v1, n1, W1 = [0], [0], 4, 10
for k in s.keys():
    w1.append(s[k].peso)
    v1.append(s[k].valor)
print(f(w1, v1, n1, W1))