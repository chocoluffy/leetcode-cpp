lst = map(int, list(raw_input().strip()))

def is_valid(lst):
    cnt = 0
    n = len(lst)
    for i in range(0, n, 1):
        cnt = cnt * 10 + lst[i]
    if cnt <= 255 and cnt >= 0:
        return True
    else:
        return False


def ip(address, limit):
    if len(address) == 0 and limit > 0:
        return 0
    if limit == 0:
        if is_valid(address):
            return 1
        else:
            return 0
    n = len(address)
    digit = 0
    cnt = 0
    for i in range(0, 3, 1):
        # print 'address = ', address, 'limit = ', limit, cnt
        index = n - i - 1
        if index <= 0:
            return cnt
        bit = address[index]
        if bit == 0: # must be a block
            cnt += ip(address[:index], limit - 2)
            return cnt
        else: # a non 0 int.
            digit = address[index] * (10**i) + digit
            if digit <= 255 and digit >= 0: # a valid digit.
                cnt += ip(address[:index], limit - 1)
            else:
                return cnt
    return cnt
            
# lst = [1, 0, 0, 0, 1]

if len(lst) < 4 or len(lst) > 12:
    print 0
else:
    print ip(lst, 3)