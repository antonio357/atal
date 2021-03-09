lis1 = [1, 12, 15, 26, 38]
lis2 = [2, 13, 17, 30, 45]

#lis1 = [1, 2, 3, 4, 5]
#lis2 = [6, 7, 8, 9, 10]

lis = []
for i in lis1:
    lis.append(i)
    
for i in lis2:
    lis.append(i)
    
i = int(len(lis) / 2)
lis = sorted(lis)
#lis = [lis[x] for x in range(len(lis) - 1, -1, -1)]

if (len(lis) % 2 == 0):
    v = lis[i] + lis[i - 1]
    v /= 2
else:
    v = lis[i]

print(lis)
print(v)
