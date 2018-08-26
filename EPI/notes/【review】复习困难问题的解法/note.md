## find majority element

Q: there is one majority element in the array, it appear more than n/2 times. 

solutions:

- binary search tree with counting. 
insert the node into binary search tree, if such leaf already exists, increase the value of that node till one exceeds n/2. for a balanced binary tree, T: O(nlogn), S: O(n), need extra n space for creating binary tree.

- moore voting(find_candidate + validate)
validate的时间是O(n)。使用类似semaphore的想法。利用一个counter，如果相邻的连续是相同的就counter++，如果不同就清零更换一个character。

## general tricks

- 相加、相乘时注意overflow的问题，在cpp和java里会出现，在python里不会。

- XOR可以用来辅助（A XOR A = 0; A XOR 0 = A）
  - even\odd apperance.
  - find missing number.
  - find duplicate.
  
- merge sort. 可以记录大小元素的先后顺序。可用于count inversions。

- quick sort. 核心在于partition，剩下的就是divide and conquer，在partition的时候，重点在O(n)的时间内，选取一个pivot，同时将所有比pivot点小的点移动到pivot左侧，比pivot点大的点移到右侧。本质上看，这个O(n)的操作，可以找到第n-index(pivot)大的元素也即pivot。可用于find k largest elements。
