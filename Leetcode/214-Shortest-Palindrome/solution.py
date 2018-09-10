"""
Given a string s, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome you can find
by performing this transformation.

Example 1:

Input: "aacecaaa" Output: "aaacecaaa" Example 2:

Input: "abcd" Output: "dcbabcd"
"""

class Solution(object):
    # naive version. search from back to front, find the longest palindrome
    # start at the first char. T: O(n^2).
    def shortestPalindrome(self, s):
        """
        :type s: str :rtype: str
        """
        if not s:
            return ""
        def is_palindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True
            # return s == s[::-1] # time consuming.
        n = len(s)
        for i in range(n-1, -1, -1):
            if is_palindrome(s[:i+1]):
                break
        remain = (n-1) - i
        pad = s[-remain:] if remain > 0 else ""
        res = pad[::-1] + s
        return res
            
        