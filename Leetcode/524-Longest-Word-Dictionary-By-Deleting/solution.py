"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
"""
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def is_subsequence(s, w):
            i = 0 
            j = 0
            while j < len(w) and i < len(s):
                if w[j] == s[i]:
                    j += 1
                    i += 1
                else:
                    i += 1
            if j == len(w) and i <= len(s):
                return True
            elif j < len(w) and i == len(s):
                return False
        new_d = sorted(d, key = lambda x: (-len(x), x))
        for w in new_d:
            if is_subsequence(s, w):
                return w
        return ""