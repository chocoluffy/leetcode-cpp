# import pprint
from collections import deque, defaultdict

M, N, K = map(int, raw_input().strip().split(" "))
table = defaultdict(lambda: [0, []])
for _ in range(K):
    s, e = map(int, raw_input().strip().split(" "))
    if e not in table:
        table[e] = [0, []]
    if s not in table:
        table[s] = [0, []]
    table[e][1].append(s)
    table[s][0] += 1
# pprint.pprint(table)

queue = deque()

for k, v in table.iteritems():
    if v[0] == 0: # outdegree = 0
        queue.append(k)

# if outdegree = 0, put into queue.
res = 0
level = 0
while len(queue) > 0:
    level += 1
    size = len(queue)
    res += (size/2 if size % 2 == 0 else (size + 1)/2)
    while(size > 0):
        size -= 1
        curr = queue.popleft()
        for source in table[curr][1]:
            table[source][0] -= 1
            if table[source][0] == 0:
                queue.append(source)
        table.pop(curr, None)

if len(table) > 0:
    print 'E'
else:
    print res