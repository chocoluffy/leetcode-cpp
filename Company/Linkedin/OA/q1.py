"""
返回substring中字典排序最小的一个。

input: "abbababzuizuizy"
output: "zy"

input: "abbababzuizuizu"
output: "zuizuizu"

一个关键的观察是，其实是返回lexicographically最大的一个suffix. 因此可以O(n)组成一个suffix array，然后直接sort.
"""

from collections import deque
def compute(s):
    # Write your code here
    if len(s) == 0:
        return ""
    stack = deque()
    stack.append((s[0], 0))
    n = len(s)
    for i in range(1, n):
        curr = s[i]
        top = stack[-1][0]
        if curr > top:
            stack = deque()
            stack.append((curr, i))
        elif curr == top:
            stack.append((curr, i))
    stack.append(('l', n+1))
    substring_lst = []
    for i in range(len(stack)-1):

        substring_lst.append()
    print stack
    first = stack[0][1]
    last = stack[-1][1]
    return s[first:last+1]
        
print compute("banananzabzb")