n, k = map(int, input().split())

max_v = int(k ** 0.5)

if n >= k:
    min_v = 1
else:
    min_v = k // n
    if k % n != 0:
        min_v += 1

count = 0

while min_v <= max_v:
    if k % min_v == 0:
        count += 1
    min_v += 1

if max_v * max_v == k:
    if count > 1:
        count = 2 * count - 1
else:
    count *= 2

print(count)
