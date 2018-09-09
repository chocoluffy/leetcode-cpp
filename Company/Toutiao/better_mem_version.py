# coding=utf-8
"""
对于lst = []
lst[1:] = []
lst[1] 会报out of boundary！
"""
n = int(raw_input())
if n == 0:
    print 3
if n == 1:
    print 2
d = map(int, raw_input().strip().split(' '))
d_sorted = sorted(d)
res = 0
i = 0
limit = 
while limit >= 0 and i < len(d_sorted) - 1:
    if limit == 0:
        limit = 2
        i += 1
    elif limit > 0 and d_sorted[i] >= d_sorted[i+1] - 10: # if [i+1] element exists.
        limit -= 1
        i += 1
    else:
        res += 1
        d_sorted[i] += 10
        limit -= 1
res += limit
print res