count = 0

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i != j and j != k and i != k and (i == 6 or j == 6 or k == 6):
               count += 1

print(count)