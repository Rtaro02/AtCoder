def shouldBreak(x, y, z):
    if x == -1 and y == -1 and z == -1:
        return False
    else:
        return False

l = list(map(int, input().split()))
N = l[0]
Y = l[1]

x = -1
y = -1
z = -1

N_10000 = 0
while N_10000 <= N:
    N_5000 = 0
    while N_5000 <= N - N_10000:
        N_1000 = N - N_10000 - N_5000
        if Y == 10000 * N_10000 + 5000 * N_5000 + 1000 * N_1000:
            x = N_10000
            y = N_5000
            z = N_1000
            break
        N_5000 += 1
    if shouldBreak(x, y, z):
        break
    N_10000 += 1
print(str(x)+ " " + str(y) + " " + str(z))