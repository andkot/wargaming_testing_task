from itertools import permutations

r = 4


def count_intial_number(sequence):
    count = 0
    for i in range(0, r):
        for j in range(i + 1, r):
            if sequence[i] > sequence[j]:
                count += 1
    return count


seq = [1, 2, 3, 4]

s = permutations(seq, r)
seqns = []
dictter = {}
for i in s:
    count = count_intial_number(i)
    if count in dictter:
        dictter[count].append(list(i))
    else:
        dictter[count] = []
        dictter[count].append(list(i))
    seqns.append(list(i))

for el in dictter:
    print(el, dictter[el])

print('--')
for el in dictter:
    for s in dictter[el]:
        for i in range(r):
            s[i] = abs(s[i] - (i + 1))
        print(s, end='')
    print()
