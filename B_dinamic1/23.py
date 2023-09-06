n = int(input())

total = [0] * (n + 1)
for i in range(2, n + 1):
    count = total[i - 1]
    if i % 2 == 0:
        count = min(count, total[i // 2])
    if i % 3 == 0:
        count = min(count, total[i // 3])

    total[i] = count + 1
print(total[-1])
i = n
mass = []
while i != 1:
    r = n
    z = n
    if i % 2 == 0:
        if total[i-1] < total[i//2]:
            r = i -1
        else:
            r = i // 2
    if i % 3 == 0:
        if total[i-1] < total[i//3]:
            z = i - 1
        else:
            z = i // 3
    if i % 3 != 0 and i % 2 != 0:
        i = i -1
    else:
        if total[z] < total[r]:
            i = z
        else:
            i = r
    mass.append(i)
mass = mass[::-1]
mass.append(n)
print(*mass)
