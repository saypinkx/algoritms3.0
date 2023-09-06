sort_mass = []


def insert(mass: list, value: int):
    mass.append(value)
    i = len(mass) - 1
    if i != 0:
        while mass[(i - 1) // 2] < mass[i] and i != 0:
            mass[i], mass[(i - 1) // 2] = mass[(i - 1) // 2], mass[i]
            i = (i - 1) // 2


def extract(mass):
    max = mass[0]
    if len(mass) == 1:
        mass.pop()
    else:
        last = mass[-1]
        mass[0] = last
        i = 0
        n = len(mass)
        while 2 * i + 1 < n and 2 * i + 2 < n:
            left = mass[2 * i + 1]
            right = mass[2 * i + 2]
            if left > right:
                z = 2 * i + 1
            else:
                z = 2 * i + 2
            if mass[i] < mass[z]:
                mass[i], mass[z] = mass[z], mass[i]
                i = z
            else:
                break
        mass.pop()
    return max


heap = []
n = int(input())
s = str(input()).split()
mass = list(map(lambda x: int(x), s))
for i in range(n):
    insert(heap, mass[i])

for j in range(n):
    elem = extract(heap)
    sort_mass.append(elem)

print(*sort_mass[::-1])
