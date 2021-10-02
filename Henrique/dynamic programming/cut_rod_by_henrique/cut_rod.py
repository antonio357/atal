from random import randint
#from sys import a

def cut_rod(p, n):
    global cut_rod_counter, cut_rod_mem
    cut_rod_counter += 1
    # print('n =', n, end=' ')
    if n == 0:
        return 0
    q = 0
    for i in range(1, n+1):
        if p.get(i):
            if not cut_rod_mem.get(n-i): q = max(q, p[i] + cut_rod(p, n-i))
            else: q = max(q, p[i] + cut_rod_mem[n-i])
    cut_rod_mem[n] = q
    return q

def cut_rod_bottom_up(p, n):
    global cut_rod_bottom_up_mem, cut_rod_bottom_up_counter
    cut_rod_bottom_up_counter += 1
    # print('n =', n, end=' ')
    if n == 0:
        return 0
    q = 0
    for i in range(n, 0, -1):
        # if i < 5: print('i =', i)
        if p.get(i):
            if not cut_rod_bottom_up_mem.get(n-i): q = max(q, p[i] + cut_rod_bottom_up(p, n - i))
            else: q = max(q, p[i] + cut_rod_bottom_up_mem[n - i])
    cut_rod_bottom_up_mem[n] = q
    # print(', q =', q)
    return q

# tem que implementar tabela como no problema da mochila
def cut_rod_bottom_up_iterative(p, rod_len):
    rod_slice_len = p
    if rod_slice_len.get(0): rod_slice_len[0] = 0
    rod_slice_len_keys = sorted(rod_slice_len.keys())
    row_len = len(rod_slice_len_keys)
    col_len = rod_len + 1
    matrix = [[0] * row_len] * (col_len)

    # for r in range(1, row_len):
    #     for c in range(1, col_len):
    #         if > :

    return matrix[row_len - 1][col_len - 1]

print('mine == expected')
for i in range(10):
    p = dict()
    for i in range(1, 51):
         p[i] = randint(5, 1000)
    l = randint(0, 20)
    cut_rod_bottom_up_mem = {}
    cut_rod_bottom_up_counter = 0
    mine = cut_rod_bottom_up(p, l)
    cut_rod_mem = {}
    cut_rod_counter = 0
    expected = cut_rod(p, l)
    print('cut_rod_counter = {}'.format(cut_rod_counter))
    print('cut_rod_bottom_up_counter = {}'.format(cut_rod_bottom_up_counter))
    if mine != expected:
        print("wrong")
        break
    print('{} == {}'.format(mine, expected))

# p = dict()
# for i in range(1, 20):
#      p[i] = randint(5, 1000)
# print(cut_rod(p, len(p.keys())))

p = {1:1, 2:2, 3:3, 4:4, 5:5}
print('\ncut_rod')
cut_rod_mem = {}
cut_rod_counter = 0
print(cut_rod(p, 4))
print('\ncut_rod_bottom_up')
cut_rod_bottom_up_mem = {}
cut_rod_bottom_up_counter = 0
print(cut_rod_bottom_up(p, 4))
print('\ncut_rod_counter = {}'.format(cut_rod_counter))
print('\ncut_rod_bottom_up_counter = {}'.format(cut_rod_bottom_up_counter))


print(cut_rod_bottom_up_iterative(p, 4))



