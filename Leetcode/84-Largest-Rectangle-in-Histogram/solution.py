class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [(-1, -1)] # (value, l_index) tuple.
        res = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            l_index = i
            while heights[i] < stack[-1][0]:
                curr = stack.pop()
                l_index = curr[1]
                res.append([curr[0], (l_index, i)]) # [value, [left, right)]
            stack.append((heights[i], l_index))
        print res
        for val, (l, r) in res:
            area = val * (r - l)
            max_area = max(area, max_area)
        return max_area

    # a more concise version:
    # - use max() dynamically update maximum, no need to use O(n) space to save value.
    # - not necessary to save value, can just save index in stack. 
    def largestRectangleArea_better(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [(-1, -1)] # (value, l_index) tuple.
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            l_index = i
            while heights[i] < stack[-1][0]:
                curr = stack.pop()
                l_index = curr[1]
                res.append([curr[0], (l_index, i)]) # [value, [left, right)]
                max_area = max(max_area, curr[0] * (i - l_index))
            stack.append((heights[i], l_index))
        return max_area

# print Solution().largestRectangleArea([2,1,5,6,2,3])
print Solution().largestRectangleArea([1])