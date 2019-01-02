num_500 = int(input())
num_100 = int(input())
num_050 = int(input())
price = int(input())

i_500 = 0
pattern = 0
while i_500 <= num_500:
    remaining_price = price - 500 * i_500
    if remaining_price < 0:
        i_500 += 1
        continue
    i_100 = 0
    while i_100 <= num_100:
        price_500 = remaining_price - 100 * i_100
        if price_500 < 0:
            i_100 += 1
            continue
        number = price_500 / 50
        if number <= num_050:
            pattern += 1
        i_100 += 1
    i_500 += 1
print(pattern)