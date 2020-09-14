output_number, diagonal = map(int, input().split())
m = [0] * output_number
n = [0] * output_number
for i in range(output_number):
    m[i], n[i] = map(int, input().split())
# #
#
# from test_c.test import *
# from random import randint


def min_side(m, n):
    if m > n:
        return n
    else:
        return m


def max_side(m, n):
    if m < n:
        return n
    else:
        return m


def is_winner(m, n, diagonal):
    _min_side = min_side(m, n)
    _max_side = max_side(m, n)
    _step_count = m + n

    if diagonal >= _min_side:
        if _step_count % 2 == 0:
            return '-'
        else:
            return '+'

    if _min_side == _max_side:
        if (_min_side // diagonal) % 2 == 0:
            if _min_side % diagonal > 0:
                return '-'
            else:
                return '+'
        else:
            if _min_side % diagonal > 0:
                return '+'
            else:
                return '-'

    if (diagonal + 1) % 2 == 0:
        if (_min_side % 2 == 0) or (_max_side % 2 == 0):
            return '+'
        else:
            return '-'
    else:
        if (_min_side % 2 != 0) or (_max_side % 2 != 0):
            return '+'
        else:
            return '-'


# m = 5
# n = 6
# d = 3
#
# print(is_winner(m, n, d))
# print(print_is_winner(m, n, d))
#
# print_table(m, n, d)


#
#
# def refactorer(n):
#     if n == 0:
#         return '-'
#     else:
#         return '+'


# while True:
#     m = randint(1, 10)
#     n = randint(1, 100)
#     d = randint(1, 100)
#     ref = refactorer(print_is_winner(m, n, d))
#     is_win = is_winner(m, n, d)
#     print(ref, is_win)
#     if ref != is_win:
#         break
#
# print(m, n, d)
# #
for i in range(output_number):
    print(is_winner(m[i], n[i], diagonal))
    # print_is_winner(m[i], n[i], diagonal)
