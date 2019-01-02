import functools

nums = list(map(int, input().split()))
N = nums[0]
A = nums[1]
B = nums[2]
sums = 0
i = 1

while i <= N:
    sum = functools.reduce(lambda x, y: x + y, list(map(int, list(str(i)))))
    if A <= sum and sum <= B:
        sums += i
    i += 1
print(sums)
