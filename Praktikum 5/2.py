x = [1,3,5,7,9]
y = [2,4,6,8,10]
z = x + y

v = 0
for j in range(len(x)):
    w = z[v]
    for i in z[v:]:
        if w > i:
            w = i
        else:
            continue
    z.remove(w)
    z.insert(v, w)
    v += 1
print(z)
