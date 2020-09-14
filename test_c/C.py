output_number, diagonal = map(int, input().split())
m = [0] * output_number
n = [0] * output_number
for i in range(output_number):
    m[i], n[i] = map(int, input().split())



# from test_c.test import *


def step_conter(m, n):
    return m + n - 2


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


def diagonal_step(diagonal):
    return diagonal * 2


def is_winner(m, n, diagonal):
    _min_side = min_side(m, n)
    _max_side = max_side(m, n)
    _diagonal_step = diagonal_step(diagonal)
    _step_count = step_conter(m, n)

    if diagonal > _min_side:
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
        if _min_side % 2 == 0 or _max_side % 2 == 0:
            return '+'
        else:
            if (_max_side - _min_side) % 2 == 0:
                return '+'
            else:
                return '-'
    else:
        if _min_side % 2 == 0 or _max_side % 2 == 0:
            return '+'
        else:
            if (_max_side - _min_side) % 2 == 0:
                return '+'
            else:
                return '-'


# m = 10
# n = 10
# d = 10
#
#
#
# print(is_winner(m, n, d))
# print_is_winner(m, n, d)
#
# print_table(m,n,d)

for i in range(output_number):
    print(is_winner(m[i], n[i], diagonal))
    # print_is_winner(m[i], n[i], diagonal)
