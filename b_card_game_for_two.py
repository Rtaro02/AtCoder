N = int(input())
a_list = list(map(int, input().split()))

sum = 0
i = 0
while len(a_list) > 0:
    number = a_list.pop(a_list.index(max(a_list)))
    if i % 2 == 0:
        sum += number
    else:
        sum -= number
    i += 1
print(sum)