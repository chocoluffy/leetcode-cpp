## find majority element

Q: there is one majority element in the array, it appear more than n/2 times. 

solutions:

- binary search tree with counting. 
insert the node into binary search tree, if such leaf already exists, increase the value of that node till one exceeds n/2. for a balanced binary tree, T: O(nlogn), S: O(n), need extra n space for creating binary tree.

- moore voting(find_candidate + validate)
validate的时间是O(n)。使用类似semaphore的想法。利用一个counter，如果相邻的连续是相同的就counter++，如果不同就清零更换一个character。

## product puzzle without division in O(n)

Q: given an array of element, return another array of same size, where each element is the product of all element except for itself. you cannot use division. do this in O(n) time.

- 构建左右累计数列。
一个很实用的技巧，当这个位置和其他所有位置的信息相关的时候，或者，如果naive的做法是基于每个点从中往外扩开的情况的话，可以考虑这个方向。也即，从左一次做累计操作，O(n)，同理从右也一遍。在本题中则是构建累乘数列，`L[i] = L[i- 1] * A[i - 1]`, `R[i - 1] = R[i] * A[i], i = n - 1, i--`. 则`prod = L[i] * R[i]`

## subarray\substring matching by hashing
应用比如 plagiarism。


## general tricks

- 大数相加、相乘时注意overflow的问题，在cpp和java里会出现，在python里不会。

- XOR可以用来辅助（A XOR A = 0; A XOR 0 = A）
  - even\odd apperance.
  - find missing number.
  - find duplicate.
  
- merge sort. 可以记录大小元素的先后顺序。可用于count inversions。

- quick sort. 核心在于partition，剩下的就是divide and conquer，在partition的时候，重点在O(n)的时间内，选取一个pivot，同时将所有比pivot点小的点移动到pivot左侧，比pivot点大的点移到右侧。本质上看，这个O(n)的操作，可以找到第n-index(pivot)大的元素也即pivot。可用于find k largest elements。

- space complexity优化的技巧。看每一次独立的遍历中依赖的变量数量。通常在dp问题里面会遇到。简单的情况是依赖于前一个或者前两个（fibonacci数列）的subproblems的答案，那么其实所需要的空间就为依赖的变量数即可，大部分dp都涉及构建一个两维的dp table，但如果每一次独立循环中问题只涉及本行和前一行的subproblems的答案，空间通常可以优化为max(row_size, column_size)，只需要每次不断地更新那一列即可。

- `y = x & !(x - 1)` will get the rightmost set bit of x. 因为(x - 1)的作用其实是反转所有rightmost set bit以右的bits。

- BST可以拓展来用于interval, number of elements in range。

- 关于heap和BST的区别：
  - 误区：heap的find max\min为O(1)，比BST更好。但其实我们可以用extra variable来拿BST的max\min从而达到同样的效果
  - 因为heap从底部插入数据，而bst是从顶部插入数据。所以heap的insert的amortized time complexity是O(1)因为最底层占了一半以上的数据。
  
- function stack也算作time complexity里。
- BST很多时候可以和divide and conquer\DP联系在一起。因为本质上每一个root都可以将range分为两个独立的range（subproblem）。结合具体问题进一步完整recursion或者dp table。
