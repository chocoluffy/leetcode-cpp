"""
When I want to loop over lines from stdin, I generally use sys.stdin instead. In that case you could ignore the count.
For a test case like the following, giving N integers and sum them up, then divide by K.

1 #test cases
3 2 #N  #K
4 5 7 #N integers 
"""

raw_input() # ignore the size
for line in sys.stdin:
    n, k = (int(i) for i in line.split())
    count = sum(int(c) for c in raw_input.split()) / k
sys.stdout.write(str(count) + "\n")
