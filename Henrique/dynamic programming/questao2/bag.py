from random import randint

def recursive(s, n, w):
    if n <= 1: return 0
    if s[n - 1].peso > w: return recursive(s, n - 1, w)
    else: return max(recursive(s, n - 1, w), s[n - 1].valor + recursive(s, n - 1, w - s[n - 1].peso))

def memoized(s, n, w, rm):
    if n <= 1: return 0
    rid = '{},{}'.format(w, n)
    if rm.get(rid): return rm[rid]
    if s[n - 1].peso > w:
        rm[rid] = memoized(s, n - 1, w, rm)
        return rm[rid]
    else:
        rm[rid] = max(memoized(s, n - 1, w, rm), s[n - 1].valor + memoized(s, n - 1, w - s[n - 1].peso, rm))
        return rm[rid]

def initMatrix(m, n, w):
    for r in range(w + 1):
        m.append(list())
        for c in range(n + 1):
            m[r].append(0)
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

for n in range(1, 63+1):
    s, w = {}, n
    for i in range(1, n+1):
        s[i] = item(randint(1, n), randint(1, n*2))

    r, mem, pd = recursive(s, n + 1, w), memoized(s, n + 1, w, {}), dynamicPrograming(s, n, w)
    if not r == pd == mem:
        print('{} | {} | {}'.format(r, mem, pd))
        print('WRONG')
        break
    print('{} == {} == {}'.format(r, mem, pd))
