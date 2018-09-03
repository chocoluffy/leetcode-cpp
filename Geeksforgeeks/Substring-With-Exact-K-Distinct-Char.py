"""
Source: https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/

Given a string of lowercase alphabets, count all possible substrings (not
necessarily distinct) that has exactly k distinct characters.

Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}
"""

class Solution():
    # T: O(n^2), S: O(k)
    def k_distinct(self, source, k):
        res = []
        for i in range(len(source)):
            counter = 0
            lookup = {}
            for j in range(i, len(source)):
                if source[j] not in lookup:
                    lookup[source[j]] = 1
                    counter = counter + 1
                if counter > k:
                    break
                if counter == k:
                    res.append(source[i:j+1])
        return len(res), res
    
    # a better version, that share one lookup table.
    def k_distinct_v2(self, source, k):
        res = []
        lookup = {}
        turn = 1
        for i in range(len(source)):
            counter = 0
            turn = turn * (-1)
            for j in range(i, len(source)):
                if source[j] not in lookup or lookup[source[j]] == turn * (-1):
                    lookup[source[j]] = turn 
                    counter = counter + 1
                if counter > k:
                    break
                if counter == k:
                    res.append(source[i:j+1])
        return len(res), res

# print Solution().k_distinct("aba", 2)
print Solution().k_distinct_v2("aba", 2)