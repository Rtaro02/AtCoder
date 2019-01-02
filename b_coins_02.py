NUM_500 = int(input())
NUM_100 = int(input())
NUM_050 = int(input())
price = int(input())

num_500 = 0
pattern = 0
while num_500 <= NUM_500:
    num_100 = 0
    while num_100 <= NUM_100:
        num_050 = 0
        while num_050 <= NUM_050:
            if price == 500 * num_500 + 100 * num_100 + 50 * num_050:
                pattern += 1
            num_050 +=1
        num_100 += 1
    num_500 += 1
print(pattern)