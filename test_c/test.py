matrix = []
matrix.append([0])

m = 5
n = 3
d = 100


def make_new_step(matrix):
    tmp_len = len(matrix)
    row = [0] * (tmp_len + 1)
    matrix.append(row)
    for i in range(tmp_len):
        matrix[i].append(0)


def check_next_step(next_el):
    if next_el == 0:
        return 1
    else:
        return 0


def fill_new_step(matrix, d=-1):
    last = len(matrix) - 1

    # vertical side
    up = 1
    diagonal = 1
    for i in range(last):
        left = matrix[i][last - 1]
        if i == d:
            diagonal = matrix[i - d][last - d]
        matrix[i][last] = check_next_step(up) or check_next_step(left) or check_next_step(diagonal)
        up = matrix[i][last]


    # horizontal side
    left = 1
    diagonal = 1
    for i in range(last):
        up = matrix[last - 1][i]
        if i == d:
            diagonal = matrix[i - d][last - d]
        matrix[last][i] = check_next_step(up) or check_next_step(left) or check_next_step(diagonal)
        left = matrix[last][i]


    # root element
    up = matrix[last - 1][last]
    left = matrix[last][last - 1]
    if last >= d and d>0:
        diagonal = matrix[last - d][last - d]
    else:
        diagonal = 1
    matrix[last][last] = check_next_step(up) or check_next_step(left) or check_next_step(diagonal)


d = 10
n = 100

for i in range(n):
    make_new_step(matrix)
    fill_new_step(matrix, d)

for row in matrix:
    print(row)
