from random import randint

rang = 4


def swap_if_true(seq, a, b):
    _min = min(a, b)
    _max = max(a, b)
    if seq[_min] > seq[_max]:
        seq[_min], seq[_max] = seq[_max], seq[_min]


def simulate(seq, final_seq):
    count = 0
    while seq != final_seq:
        a = randint(0, rang - 1)
        b = randint(0, rang - 1)
        if a != b:
            swap_if_true(seq, a, b)
            count += 1
    return count


def simulate_n(seq, final_seq, count):
    n = 0
    for i in range(count):
        _seq = list.copy(seq)
        n += simulate(_seq, final_seq)
    return n


def count_prop_n(seq, final_seq, count, n):
    num = 0
    for i in range(count):
        _seq = list.copy(seq)
        if n == simulate(_seq, final_seq):
            num += 1
    return num / count


final_seq = [1, 2, 3,4]
# seq = [,, , , ]
seq = [4, 2, 1, 3]
count = 100000

n = simulate_n(seq, final_seq, count)
print(n / count)

# row = [0]*1000
# for i in range(1000):
#     tmp = count_prop_n(seq, final_seq, count, i)
#     row[i] = tmp
#     print(i, tmp)
#
# with open('data.txt', 'w') as file:
#     for i in row:
#         file.writelines(str(i))
#         file.writelines('\n')
