n = int(raw_input())
lst = map(int, raw_input().strip().split(' '))

def valid(d, start, size):
    for i in range(start + 1, start + size + 1):
        after = d[i] >> 6
        if i >= len(d) or after != 0b10:
            return False
    return True

i = 0
res = False
while i < len(lst):
    k = lst[i]
    if (k >> 3) == 0b11110 and valid(lst, i, 3):
        i += 4
    elif (k >> 4) == 0b1110 and valid(lst, i, 2):
        i += 3
    elif (k >> 5) == 0b110 and valid(lst, i, 1):
        i += 2
    elif (k >> 7) == 0:
        i += 1
    else:
        res = False
        break
if i >= len(lst):
    print 1
else:
    print 0