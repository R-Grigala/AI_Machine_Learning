
t1 = (5, 'a')
t2 = (7, 'b')
t3 = (9, 'c')

t4 = (6, 'd')

l1 = [t1, t2, t3]
print(l1)

inserted = False
for i in range(len(l1 )):
    if t4[0] < l1[i][0]:
        l1.insert(i, t4)
        break
else:
    l1.append(t4)

print(l1)