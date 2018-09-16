"""
'leetcode'

=> 

'leetcode '

when i points the last padding position. 

dp[i]: if everything before i position can be contained in dictionary.


## review:
- BFS does not suitful for string match, especially for prefix\suffix problem,
  because subproblem can be exponential in worse case(word in wordDict are all
  prefix to each other)!

- while in this case, it is helpful to use DFS with heuristics that we search
  with the longer word first, then shorter one.

- BFS在matrix中不容易出现这种subproblem overlap的问题，但是在string的问题上，容
  易出现重复的子问题。这种时候需要一个visited[]，保证只去探索没有探索过的子问
  题。

"""
from collections import deque
class Solution(object):
    # dynamic programming.
    def wordBreak(self, s, wordDict):
        """
        :type s: str :type wordDict: List[str] :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1) # add one more padding to the end of the string.
        dp[0] = True # for base case when i = 0, meaning empty string can be formed in dictionary, thus first char only depands on if the first char is in the dictionary
        for i in range(1, n+1):
            for j in range(0, i):
                # print j, dp[j], s[j:i]
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        # print dp
        return dp[n]

    # dp v2. use word dict to match, instead of using j to iterate.
    # because, assume that `s[j:i] in wordDict` is expensive.
    # 63.42%
    def wordBreak_v3(self, s, wordDict):
        """
        :type s: str :type wordDict: List[str] :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1) # add one more padding to the end of the string.
        dp[0] = True # for base case when i = 0, meaning empty string can be formed in dictionary, thus first char only depands on if the first char is in the dictionary
        for i in range(1, n+1):
            for w in wordDict:
                w_len = len(w)
                if i - w_len >= 0 and dp[i - w_len] and s[i - w_len:i] == w:
                    dp[i] = True
        # print dp
        return dp[n]

    # BFS.
    # 100%
    def wordBreak_v2(self, s, wordDict):
        n = len(s)
        visited = [False] * n
        queue = deque()
        queue.append("")
        while len(queue) > 0:
            while len(queue) > 0:
                curr = queue.popleft()
                curr_len = len(curr)
                if not visited[curr_len]: # avoid re-visiting same sub problems.
                    for w in wordDict:
                        w_len = len(w)
                        if curr_len + w_len == len(s) and curr + w == s:
                            return True
                        if w == s[curr_len:curr_len+w]:
                            queue.append(curr + w_len)
                visited[curr_len] = True
        return False
        
print Solution().wordBreak('leetcode', ['leet', 'code'])
