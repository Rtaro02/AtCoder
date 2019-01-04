def canContinue(d, p):
    distance = abs(d[p][1] - d[p - 1][1]) + abs(d[p][2] - d[p - 1][2])
    if d[p][0] - d[p - 1][0] < distance:
        return False
    remaining_action = d[p][0] - d[p - 1][0] - distance
    if remaining_action % 2 == 0:
        return True
    else:
        return False

N = int(input())
d = []
d.append([0,0,0])
i = 0
while i < N:
    d.append(list(map(int, input().split())))
    i += 1
position = 1
answer = True
while position < N + 1:
    if canContinue(d, position):
        i += 1
    else:
        answer = False
        break
    position += 1
if answer:
    print("Yes")
else:
    print("No")