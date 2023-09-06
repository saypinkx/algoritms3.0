n = int(input())

a = [3600] * 3
b = [3600] * 3
c = [3600] * 3

for i in range(n):
    string = str(input()).split()
    mass = list(map(lambda x: int(x), string))
    a.append(mass[0])
    b.append(mass[1])
    c.append(mass[2])

x = [0, 0, 0]
for i in range(3, n + 3):
    y = min(a[i] + x[i - 1], x[i - 2] + b[i - 1], x[i - 3] + c[i - 2])
    x.append(y)

print(x[-1])
