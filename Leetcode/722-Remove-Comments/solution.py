"""

record valid /* start index, and mark delete mode; 
after each string, if not end index, then delete
till the end. and mark the start index = 0 (meaning for all later string, start
deleting from the start)

"""
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str] 
        :rtype: List[str]
        """
        for s in source:
            n = len(s)
            for i in range(0, n-1): # mind the last char.
                if s[i] == '/' and s[i+1] == '/'

        