# coding=utf-8
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    d_lst = map(int, line.split())
    d_sorted = sorted(d_lst)
    def count_d(lst, limit):  # i counts down.
    	if not lst:
			return limit
    	if limit <= 0:
        	return count_d(lst[1:], 2)  # if lst[1] exists.
		if limit > 0:
			if lst[0] - lst[1] <= 10: # if lst[1] exists.
				return count_d(lst[1:], limit - 1)
        	else:
				return 1 + count_d([lst[:i], lst[i] + 10, lst[i+1:]], limit - 1)
    res = count_d(d_sorted, 2)
    print res