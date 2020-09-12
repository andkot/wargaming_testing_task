# output_number, diagonal = map(int, input().split())
# m = [0] * output_number
# n = [0] * output_number
# for i in output_number:
#     m, n = map(int, input().split())


def step_conter(m, n):
    return m + n - 2

def min_side(m,n):
    if m > n:
        return n - 1
    else:
        return m - 1

def is_winner(step_count, diagonal, min_side):
    if diagonal > min_side:
        print('diag >')
        if step_count % 2 == 0:
            return '-'
        else:
            return '+'
    elif diagonal == min_side:
        print('diag =')
        return '+'
    elif diagonal == 1:
        print('diag = 1')
        if step_count % 2 == 0:
            return '-'
        else:
            return '+'
    else:
        print('else')
        shift = step_count // (diagonal + 1)
        print(shift)
        if step_count % 2 != 0 and shift % 2 != 0:
            return '-'
        else:
            return '+'


print(is_winner(step_conter(10, 10), 20))
