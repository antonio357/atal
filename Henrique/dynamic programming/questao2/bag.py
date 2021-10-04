from random import randint

def printMatrix(m):
    print()
    for i in m: print(i)

def initMatrix(m, n, w):
    for r in range(w + 1):
        m.append(list())
        for c in range(n + 1):
            m[r].append(0)

def recursive(s, n, w):
    if n <= 1: return 0
    elif s[n - 1].peso > w: return recursive(s, n - 1, w)
    else: return max(recursive(s, n - 1, w), s[n - 1].valor + recursive(s, n - 1, w - s[n - 1].peso))

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

brk = False
for n in range(1, 10+1):
    s, sr, ws, vs = {}, {}, [], []
    for i in range(1, n+1):
        s[i] = item(randint(1, 100), abs(sum([x.peso for x in s.values()]) - randint(1, 100)) if i % 2 == 0 else sum([x.peso for x in s.values()]) + randint(1, 100))
        sr[i - 1] = s[i]
    for k in s.keys():
        if k != 0:
            ws.append(s[k].peso)
            vs.append(s[k].valor)

    for w in range(0, n*2):
        expected, found_r = dynamicPrograming(s, n, w), recursive(s, n+1, w)
        if not expected == found_r:
            print('{} | {}'.format(expected, found_r))
            print('WRONG')
            brk = True
            break
        print('{} == {}'.format(expected, found_r))

    if brk: break


# s = {
#     1: item(6, 30),
#     2: item(3, 14),
#     3: item(4, 16),
#     4: item(2, 9)
# }
# n, w = 4, 10
#
# print('expected', dynamicPrograming(s, n, w))
# # print(recursive(s, n, w))
# w1, v1, n1, W1 = [], [], n, w
# for k in s.keys():
#     w1.append(s[k].peso)
#     v1.append(s[k].valor)
# # print('f(n, W)')
# # print('f({}, {})'.format(n1, W1))
# print('try', f(w1, v1, n1, W1))
# print('my try', f_with_dict(s, n, w))