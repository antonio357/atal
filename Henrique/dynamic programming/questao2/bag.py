def printMatrix(m):
    print()
    for i in m: print(i)

def initMatrix(m, n, w):
    for r in range(w + 1):
        m.append(list())
        for c in range(n + 1):
            m[r].append(0)

def f(w, v, n, W, id=0, idP=-1, idc=None, idcP=None):
    # print('f({}, {}), id = {}, idP {}, idc = {}, idcP = {}'.format(n, W, id, idP, idc, idcP))
    # print('f({}, {}, {}, {})'.format(w, v, n, W))
    # print(n, end=' ')
    if n <= 0:
        # print('end')
        return 0
    elif w[n - 1] > W:
        # print('f({}, {}), elif'.format(n - 1, W))
        return f(w, v, n - 1, W, id + 1, id, '/', idc)
    else:
        # print('f({}, {}), else, first'.format(n - 1, W))
        x1 = f(w, v, n - 1, W, id + 1, id, '//', idc)
        # print('f({}, {}), else, then'.format(n - 1, W - w[n - 1]))
        x2 = v[n - 1] + f(w, v, n - 1, W - w[n - 1], id + 1, id, '///', idc)
        return max(x1, x2)

def getFromdit(dit, key):
    if dit.get(key):
        return dit[k]
    return item(-1, -1)

def f_with_dict(items_value_weight, current_item, current_weight):
    if current_item <= 0: return 0
    elif getFromdit(items_value_weight, current_item - 1).peso > current_weight: return f_with_dict(items_value_weight, current_item - 1, current_weight)
    else:
        return max(f_with_dict(items_value_weight, current_item - 1, current_weight), getFromdit(items_value_weight, current_item).valor + f_with_dict(items_value_weight, current_item - 1, current_weight - getFromdit(items_value_weight, current_item - 1).peso))

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

print('expected', dynamicPrograming(s, n, w))
# print(recursive(s, n, w))
w1, v1, n1, W1 = [], [], n, w
for k in s.keys():
    w1.append(s[k].peso)
    v1.append(s[k].valor)
# print('f(n, W)')
# print('f({}, {})'.format(n1, W1))
print('try', f(w1, v1, n1, W1))
print('my try', f_with_dict(s, n, w))