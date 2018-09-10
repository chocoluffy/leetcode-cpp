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
            

    # better version, inspired from KMP pattern matching algorithm, find out the
    # longest prefix\suffix match for a new string s#rev(s) in O(n).
    def shortestPalindrome_v2(self, s):
        new_s = s + "#" + s[::-1]
        n = len(new_s)
        table = [0] * n # record the longest prefix\suffix match
        p_last = 0
        for i in range(1, n):
            if new_s[p_last] == new_s[i]: # find new match between prefix and suffix.
                table[p_last] = p_last
                p_last += 1
            else:
                
        