class Solution(object):
    # mem limit exceeded.
    def wordBreak_v1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # use set to check if string breakable first.
        s_set = set(list(s))
        dict_set = set([c for c in list(w) for w in wordDict])
        for c in s_set:
            if c not in dict_set:
                return []
                
        n = len(s)
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for i in range(1, n+1):
            for w in wordDict:
                w_len = len(w)
                if i - w_len >= 0 and len(dp[i - w_len]) > 0 and s[i - w_len:i] == w:
                    for c in dp[i - w_len]:
                        new_s = c + " " + w
                        dp[i].append(new_s.strip())
        return dp[n]

    # memo with back-track.
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                        for j in range(i+1, len(s)+1)
                        if s[i:j] in wordDict
                        for tail in sentences(j)]
            return memo[i]
        return sentences(0)
    
        
print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])