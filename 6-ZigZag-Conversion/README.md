# 思路(C++)

重点在algorithm.

## intuition

find pattern in blocks.

say `numrows = n`, then group n + (n - 2) elements as one group. and assign each of it into one bucket, and finally concatenate bucket contents together.

- string array. in cpp, use char[][] to represent string array.

- construct and return char array requires to put an endline character at the end.