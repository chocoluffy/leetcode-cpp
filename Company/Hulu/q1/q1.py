n = int(raw_input().strip())
lst = []
for _ in range(n):
    num = int(raw_input().strip())
    lst.append(num)
lst = [[v, i] for i, v in enumerate(lst)]
lst = sorted(lst, key = lambda x: x[0])
# print lst
cnt = 0
prev = None
for i in range(n):
    if lst[i][0] == prev:
        tmp = lst[i][0]
        lst[i][0] = lst[i-1][0]
        cnt += tmp
        prev = tmp
    else:
        tmp = lst[i][0]
        lst[i][0] = cnt
        cnt += tmp
        prev = tmp
res = map(lambda x: x[0], sorted(lst, key = lambda x: x[1]))
for v in res:
    print v
# print res
