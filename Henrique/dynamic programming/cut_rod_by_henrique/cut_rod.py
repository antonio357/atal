from random import randint
#from sys import a

def cut_rod(p, n):
    global cut_rod_counter, cut_rod_mem
    cut_rod_counter += 1
    if n == 0:
        cut_rod_mem[0] = 0
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
        cut_rod_bottom_up_mem[0] = 0
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

# def cut_rod_bottom_up_iterative(p, n):
#     arr, q = [0], 0
#     for i in range(n, 0, -1):
#         q = max(q, p[i] + cut_rod_bottom_up(p, n - i))
#     return

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

# p = {1:1, 2:2, 3:3, 4:4, 5:5}
# print('\ncut_rod')
# cut_rod(p, 4)
# print('\ncut_rod_bottom_up')
# cut_rod_bottom_up(p, 4)
