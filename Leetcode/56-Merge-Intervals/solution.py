# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        sorted_inv = sorted(intervals, key=lambda i:i.start)
        res = []
        i = 0
        while i < len(sorted_inv):
            start = sorted_inv[i].start
            end = sorted_inv[i].end
            while i < len(sorted_inv) and sorted_inv[i].start <= end:
                end = max(end, sorted_inv[i].end)
                i = i + 1
            res.append([start, end])
        return res
            