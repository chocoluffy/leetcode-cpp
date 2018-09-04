"""
Input:
"a"
"aa"

Expected:
""
"""

from collections import Counter
class Solution(object):
    # should not use set, if t can contain duplicate chars.
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        unvisited_set = set(list(t))
        cnt = Counter()
        l = 0
        min_l = float('inf')
        start_index = -1
        for i in range(len(s)):
            # print s[i], unvisited_set, cnt
            if s[i] in t:
                if cnt[s[i]] == 0:
                    unvisited_set.remove(s[i])
                cnt[s[i]] += 1
            if len(unvisited_set) == 0: # all target chars visited, move left pointer to shrink and keep property.
                while(len(unvisited_set) == 0):
                    if s[l] in t:
                        cnt[s[l]] -= 1
                        if cnt[s[l]] == 0:
                            unvisited_set.add(s[l])
                    l += 1
                curr_len = i - (l-1) + 1
                if curr_len < min_l:
                    min_l = curr_len
                    start_index = l-1
        return s[start_index: start_index + min_l]        

print Solution().minWindow("ADOBECODEBANC", "ABC")