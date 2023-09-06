string = str(input()).split()
n = int(string[0])
k = int(string[1])
base = [1, 1]
if k == 1 or n==1:
    print(1)
else:
    for i in range(2, k + 1):
        base.append(base[i -1] * 2)




    for j in range(i + 1, n):
        base.append(sum(base[j-k:j]))


    if n-1 ==0:
        print(1)
    else:
        print(base[n-1])

