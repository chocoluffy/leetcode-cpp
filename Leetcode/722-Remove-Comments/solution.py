"""

Input: ["a/*comment", "line", "more_comment*/b"] Output: ["a","b"] Expected:
["ab"]


A good edge case: meaning that we only create new empty new_s [], when it's in
search mode. since after removing several lines, for the next line, if we have
some char remained, we need to append it to the previous string output instead
of a new string.

Some good coding practice review:
- when we need to examine two char to match a pattern. how to handle that in
  for\while loop, especially, how we handle the last char.

> use more slicing operation! instead of index accessing operation to avoid the
> boundary checking.

"""
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str] :rtype: List[str]
        """
        res = []
        mode = 0 # 0: search mode, 1: delete mode.
        for s in source:
            n = len(s)
            if mode == 0:
                new_s = []  
            i = 0
            while i < n:
                if s[i:i+2] == '//' and mode == 0: # search mode
                    break
                elif s[i:i+2] == '/*' and mode == 0:
                    mode = 1
                    i += 1 # avoid edge case like '/*/'
                elif s[i:i+2] == '*/' and mode == 1:
                    mode = 0
                    i += 1
                elif mode == 0:
                    new_s.append(s[i])
                i += 1
            if mode == 0 and len(new_s) > 0:
                res.append("".join(new_s))
        return res


# v2
class Solution(object):
    def removeComments(self, source):
        in_block = False
        ans = []
        for line in source:
            i = 0
            if not in_block:
                newline = []
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    newline.append(line[i])
                i += 1
            if newline and not in_block:
                ans.append("".join(newline))

        return ans