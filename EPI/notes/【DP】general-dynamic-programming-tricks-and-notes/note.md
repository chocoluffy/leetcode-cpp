## padding and index
usually we need to set base case.
like for dp in strings, the base case is usually empty string. 
thus we enlarge the usual dp table by increasing the height and width by 1.
but when we iterate the table, and refer to the original string, we need to reduce the index by 1 to match with original string index.
还是看情况的，主要依据是根据dp里和occurrence的联系来判断的，dp[i]如果和dp[i-1]等相关，则往往是在前面添加padding。如果dp[i]和dp[i+1]相关，则在后面添加padding。

## dp table里index的含义
搞清楚index i，dp[i]表示的是，从开始到包含i这个位置的元素[:i+1]，还是直到i这个位置之前[:i]，还是指从后开始的。

经典例子：LC139 word break。
采用dp[i]：因为base case当字符串为""时，应当是true，则dp[i]表示的是，当i位置之前的字符串是否满足题意。因此需要在结尾多pad一位，并最终返回的是dp[n]。

## hard DP intuition

- 反向思考

当正向思考的时候会带来过多的subproblems，而subproblems之间又难以合理应用memorization的时候。因为DP的种类其实就两种，一种是top-bottom+cache(memorization)的解决方式，另外一种是bottom-up。当正向的subproblem不重叠又指数增长的时候，divide and conquer也没有用，因为divide and conquer并不会减少子问题的数量。可以尝试反向去思考bottom-up的方式。例如，一个个数减少的时候，可以尝试从没有开始一个个数增加。典型例子，LC312 Burst Balloon. 

> 什么时候需要反向思考: 当正向思考的时候，发现当先的最优解会被后来的发现(exploration)而更新的时候！可以考虑逆向的思考！逆向的保证，可以保证子问题的最优结构保持住！

比如一个简单的例子：
LC64.Minimum Path Sum，在一个矩阵中找到从左上到右下的最短距离。
如果正向思考，会发现当前积累的最短距离可能并不是，未来如果有发现新的路径，会更新现在的最优解。于是考虑逆向思考！当从*终点一个点*的时候开始，不断expand，由于最短路径的子问题也是保持最短路径，因此遍历的时候只需要保持来自down或者right方向上的最小值即可。

LC312.Burst Balloon，扎破气球的时候获得积分来自自己和自己的邻居。求扎完全部气球的时候的最大积分。
如果正向思考会发现，选取扎破这个气球的到的当前最大积分很可能不是最优解，会被其他选择的未来所更新。因此考虑逆向思考！由于是一个个扎破气球，最后的情况是只剩下边缘。于是开始从两个boundary开始往中间添加气球，这个操作会是正向思考问题时候的最后一步。然后再考虑往哪一边继续添加气球。特别注意算法的实现方式，利用了一个window size不断expand的思路，可视化之后是一个矩形从中间往边缘扩散的模型。

- 中心边缘扩散类

总结一下这一类型叫做中心往边缘扩散类型。特别适用于一种情况下的动态规划：每个问题和其周围边缘的子问题相关。转换为子问题的方式是向四周扩散或者向中心缩小。同样很直观的是，其在矩形里的遍历规律是，先把对角线位置的补齐，然后从对角线往边缘遍历。

典型例子：LC312 Burst Ballon; LC5 Longest Palindrome; Matrix Chain Multiplication.
典型解法：
```python
for window in range(1, n):
	for i in range(0, n-window):
    	right = i + window
```


- 动态式

每个当前状态和所有上一层级的子问题都相关。比如Ladder Climbing。

- 2维数组，代表两种不同的限制
构建D[i][j]， j可以表示两者之差，如果最后希望拿到的是相等的值，即设j=0。例子，今日头条面经题目，个人得分和团体得分。以及典型的背包问题，第一个i表示item，第二个j表示重量限制。