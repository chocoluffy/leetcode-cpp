try:
    s = raw_input().strip()
except EOFError:
    print 0

max_l = 0
set_s = set()
length = 0
for i in range(len(s)):
    if s[i] not in set_s:
        set_s.add(s[i])
        length += 1
        max_l = max(max_l, length)
    else:
        set_s = set()
        set_s.add(s[i])
        length = 1

print max_l