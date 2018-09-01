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
        stack = [-1] # store index in stack.
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                curr = stack.pop()
                l_index = stack[-1]
                max_area = max(max_area, heights[curr] * (i - l_index -1))
            stack.append(i)
        return max_area

print Solution().largestRectangleArea_better([2,1,5,6,2,3])
# print Solution().largestRectangleArea_better([2, 1, 2])