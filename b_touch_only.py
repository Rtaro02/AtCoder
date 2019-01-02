def containOdd(x):
    for c in x:
        if c % 2 == 1:
            return True
    return False

l = int(input())
nl = list(map(int, input().split()))
i = 0
while not containOdd(nl):
    nl = list(map(lambda x: x/2, nl))
    i += 1
print(i)