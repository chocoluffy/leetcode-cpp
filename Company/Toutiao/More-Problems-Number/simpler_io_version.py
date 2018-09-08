# coding=utf-8
"""
对于lst = []
lst[1:] = []
lst[1] 会报out of boundary！
"""
n = int(raw_input())
a = raw_input()
d = map(int, raw_input().strip().split(' '))
d_sorted = sorted(d)
def count_d(lst, limit):  # i counts down.
    if len(lst) <= 1:
        return limit
    if limit <= 0:
        return count_d(lst[1:], 2)
    if limit > 0:
        if lst[0] - lst[1] <= 10: # if lst[1] exists.
            return count_d(lst[1:], limit - 1)
        else:
            return 1 + count_d([lst[:i], lst[i] + 10, lst[i+1:]], limit - 1)
res = count_d(d_sorted, 2)
print res