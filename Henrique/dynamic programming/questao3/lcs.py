def recursive(X, Y, x, y):
    if x == 0 or y == 0: return 0
    elif X[x - 1] == Y[y - 1]: return recursive(X, Y, x - 1, y - 1) + 1
    else: return max(recursive(X, Y, x, y - 1), recursive(X, Y, x - 1, y))


def memoized(X, Y, m, n):
    C = [[None] * (n + 1) for i in range(m + 1)]
    return memoized_recursion(X, Y, C, len(X), len(Y))

def memoized_recursion(X, Y, C, x, y):
    if C[x][y] == None:
        if x == 0 or y == 0: C[x][y] = 0
        elif X[x - 1] == Y[y - 1]: C[x][y] = memoized_recursion(X, Y, C, x - 1, y - 1) + 1
        else: C[x][y] = max(memoized_recursion(X, Y, C, x, y - 1), memoized_recursion(X, Y, C, x - 1, y))
    return C[x][y]


def dynamicPrograming(X, Y, m, n):
    C = [[None] * (n + 1) for i in range(m + 1)]
    for x in range(m + 1): C[x][0] = 0
    for y in range(n + 1): C[0][y] = 0

    for x in range(m + 1):
        for j in range(n + 1):
            if x == 0 or y == 0:
                C[x][y] = 0
            elif X[x - 1] == Y[y - 1]:
                C[x][y] = C[x - 1][y - 1] + 1
            else:
                C[x][y] = max(C[x - 1][y], C[x][y - 1])

    return C[m][n]

test_cases = [
    ["ABCBDAB", "BDCABA"],
    ["ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"],
    ["ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA"]
]

for t in test_cases:
    X, Y = t[0], t[1]
    m, n = len(X), len(Y)
    r, m = recursive(X, Y, m, n), memoized(X, Y, m, n)
    print(r, m)