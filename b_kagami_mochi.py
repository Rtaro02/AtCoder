N = int(input())
l = []
i = 0
while i < N:
    l.append(int(input()))
    i += 1

size = 0
tmp = -1
while len(l) > 0:
    if tmp != max(l):
       size += 1
    tmp = max(l)
    l.remove(max(l))
print(size)