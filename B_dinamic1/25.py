n = int(input())
s = str(input()).split()
mass = list(map(lambda x: int(x), s))
mass = sorted(mass)
result = [1000]
result.append(mass[1] - mass[0])

for i in range(2, n):
    l = mass[i] - mass[i - 1]
    if i == n:
        result.append(result[i - 1] + l)
    else:
        result.append(min(result[i - 1], result[i - 2]) + l)


print(result[-1])
