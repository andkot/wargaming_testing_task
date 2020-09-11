balance = 100  # int(input())
price = [21, 34, 18, 435, 18, 34, 20, 21, 19]  # list(map(int, input().split()))
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_digit = 9

tmp = digits[0]


def find_min(numbers, digits):
    min_value = numbers[0]
    tmp_digit = digits[0]
    for i in range(1, 9):
        if min_value >= numbers[i]:
            min_value = numbers[i]
            tmp_digit = digits[i]
    return min_value, tmp_digit


min_price, tmp = find_min(price, digits)
number_runk = balance // min_price

if number_runk == 0:
    print(-1)
else:
    remainder = balance % min_price
    max_number = [tmp] * number_runk
    n = 0
    while remainder > 0 and n < number_runk:
        shift = 0
        while tmp < max_digit:
            if remainder >= price[tmp] + price[tmp]:
                remainder = remainder + min_price - price[tmp]
                min_price = price[tmp]
                max_number[n] = digits[tmp]
                tmp += 1
            else:
                tmp += 1
        tmp = old_tmp
        min_price = old_min_price
        n += 1

    print(''.join(map(str, max_number)))
