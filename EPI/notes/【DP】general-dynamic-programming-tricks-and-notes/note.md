## padding and index
usually we need to set base case.
like for dp in strings, the base case is usually empty string. 
thus we enlarge the usual dp table by increasing the height and width by 1.
but when we iterate the table, and refer to the original string, we need to reduce the index by 1 to match with original string index.

## hard DP intuition

- 反向思考

当正向思考的时候会带来过多的subproblems，而subproblems之间又难以合理应用memorization的时候。因为DP的种类其实就两种，一种是top-bottom+cache(memorization)的解决方式，另外一种是bottom-up。当正向的subproblem不重叠又指数增长的时候，divide and conquer也没有用，因为divide and conquer并不会减少子问题的数量。可以尝试反向去思考bottom-up的方式。例如，一个个数减少的时候，可以尝试从没有开始一个个数增加。典型例子，LC312 Burst Balloon. 

- 动态式

每个当前状态和所有上一层级的子问题都相关。

- 