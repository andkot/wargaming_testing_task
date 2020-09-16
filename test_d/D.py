# t = int(input())
# a = []
# for i in range(t):
#     a.append(list(map(int, input().split())))
# print(a)

P0 = 1 / 45
N0 = 45
RANG = 4
N0 = int(RANG * (RANG - 1) / 2)


def count_intial_number(sequence):
    count = 0
    for i in range(0, RANG):
        for j in range(i + 1, RANG):
            if sequence[i] > sequence[j]:
                count += 1
    return count


def find_elem_num(sequence, value):
    for i in range(0, RANG):
        if sequence[i] == value:
            return i


def count_min_number(sequence):
    tmp = list.copy(sequence)
    count = 0
    # step = 0
    # print(sequence)
    # a0 = count_intial_number(seq)
    # print(a0)
    # print('----------')
    for i in range(0, RANG):
        if tmp[i] != i + 1:
            num = find_elem_num(tmp, i + 1)
            tmp[i], tmp[num] = tmp[num], tmp[i]
            count += 1
            # print(sequence)s
            # a1 = count_intial_number(seq)
            # print(a1, a0 - a1)
            # a0 = a1
    return count


def count_fact(n):
    if n == 0:
        return 1
    else:
        return n * count_fact(n - 1)


def count_p_min(n_min):
    return (1 / (N0 ** n_min)) * count_fact(n_min)


def get_all_move(sequence, tab):
    # print('initial: ', count_intial_number(sequence))
    for i in range(0, RANG):
        for j in range(i + 1, RANG):
            if sequence[i] > sequence[j]:
                sequence[i], sequence[j] = sequence[j], sequence[i]
                count = count_intial_number(sequence)
                print(f'{tab} {count}: {sequence}: min {count_min_number(sequence)} const: {N0 - count}')
                # print(f'{tab} {sequence}')
                get_all_move(sequence, tab + '\t')

                sequence[i], sequence[j] = sequence[j], sequence[i]


# print(P0)
#
# s = 0
# for i in range(1, 100000):
#     s = s + ((1 - P0) ** (i - 1)) * (P0) * i
#
# print(s)

seq = [4, 3, 2, 1]
# print(count_min_number(seq))
# print('------------------------------')

# print(count_intial_number([2, 4, 3, 1]))
# print(count_intial_number([2, 1, 3, 4]))
# print(count_intial_number([1, 2, 3, 4]))
# seq = [9, 7, 10, 5, 6, 8, 1, 2, 3, 4]
# print(count_intial_number(seq))
# print(count_min_number(seq))

# print(count_p_min(6))
#

# import sys
# sys.stdout = open('file', 'w')

print(f"{count_intial_number(seq)}: {seq}: min {count_min_number(seq)} const: {N0 - count_intial_number(seq)}")
get_all_move(seq, '\t')

# print(count_intial_number(seq))
# print(count_min_number(seq))
