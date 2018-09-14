"""

Input:
["a/*comment", "line", "more_comment*/b"]
Output:
["a","b"]
Expected:
["ab"]


A good edge case:
meaning that we only create new empty new_s [], when it's in search mode.
"""
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str] 
        :rtype: List[str]
        """
        res = []
        mode = 0 # 0: search mode, 1: delete mode.
        for s in source:
            n = len(s)
            if mode == 0:
                new_s = []  
            i = 0
            stop = False
            while i < n-1: # mind the last char.
                if s[i] == '/' and s[i+1] == '/' and mode == 0:
                    res.append("".join(new_s))
                    stop = True
                    break
                elif s[i] == '/' and s[i+1] == '*' and mode == 0:
                    # switch to delete mode.
                    mode = 1
                    i += 1
                elif s[i] == '*' and s[i+1] == '/' and mode == 1:
                    # switch to search mode.
                    mode = 0
                    i += 2
                else: # other cases. 
                    if mode == 0:
                        new_s.append(s[i])
                    i += 1
            if i == n-1 and mode == 0 and not stop:
                new_s.append(s[i])
            if not stop:
                string = "".join(new_s)
                if len(string) > 0:
                    res.append(string)
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