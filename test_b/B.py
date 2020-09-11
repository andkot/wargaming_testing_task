balance = int(input())  # 100
price = list(map(int, input().split()))  # [21, 34, 18, 435, 18, 34, 20, 21, 19]
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


min_price, min_digit = find_min(price, digits)
number_runk = balance // min_price

if number_runk == 0:
    print(-1)
else:
    remainder = balance % min_price
    max_number = [min_digit] * number_runk
    n = 0
    while remainder > 0 and n < number_runk:
        shift = 1
        tmp = min_digit
        while tmp < max_digit:
            if remainder + price[tmp - shift] >= price[max_digit - shift]:
                max_number[n] = digits[max_digit - shift]
                remainder = remainder + price[tmp - shift] - price[max_digit - shift]
                break
            else:
                max_digit -= 1
        n += 1

    print(''.join(map(str, max_number)))
