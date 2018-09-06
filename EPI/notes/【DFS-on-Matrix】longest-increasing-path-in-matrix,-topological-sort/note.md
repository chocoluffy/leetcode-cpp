这个帖子主要记录，如果将matrix问题转化为graph的问题，并结合topological sort来解决：

- 遍历图中每个点，找到每个点的outgoing degree，和其neighbor相比较。

相关问题：
- [longest increasing path](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)