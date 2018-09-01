"""
- Construct a matrix by a bottom-up fashion, each entry record (m, n), meaning
  the consecutive 1s in two directions as bottom and right. Such as at position
  (i, j), there are m consecutive 1s from current position towards the bottom,
  and n such consecutive 1s towards the right. 

- then one more pass to find out the maximum area from the matrix entry.


# challenge:
- inner list being updated at the same time. but not individually! mind such
  reference error.
- handle the base case in the matrix form, especially the case:
    - empty matrix.
    - single row matrix.
"""
import pprint


class Solution(object):

    def maximalRectangle_better(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * (len(matrix[0])+1)
        max_area = 0
        for row in matrix:
            for i in xrange(len(row)): # update height
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in xrange(len(matrix[0])+1):
                while heights[i] < height[stack[-1]]:
                    height = heights[stack.pop()]
                    l_index = stack[-1]
                    max_area = max(max_area, height * (i - 1 - l_index))
                stack.append(i)
        return max_area


    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]] :rtype: int
        """
        if not matrix:
            return 0
        table = [[(0, 0)] * (len(matrix[0]) + 1)
                 for _ in range(len(matrix) + 1)]
        # update right direction count.
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                this_lst = list(table[i][j])
                if matrix[i][j] == '1':
                    this_lst[1] = table[i][j+1][1] + 1
                else:
                    this_lst[1] = 0
                table[i][j] = tuple(this_lst)

        # update bottom direction count.
        for i in range(len(matrix[0]) - 1, -1, -1):
            for j in range(len(matrix) - 1, -1, -1):
                this_lst = list(table[j][i])
                if matrix[j][i] == '1':
                    this_lst[0] = table[j+1][i][0] + 1
                else:
                    this_lst[0] = 0
                table[j][i] = tuple(this_lst)

        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                x = float('inf') if j+1 == len(matrix[0]) else table[i][j+1][0]
                y = float('inf') if i+1 == len(matrix) else table[i+1][j][1]
                validator = (x, y)
                # print i, j, validator
                if table[i][j][0] == 1 or table[i][j][1] == 1 or (table[i][j][0] <= validator[0] and table[i][j][1] <= validator[1]):
                    current_area = table[i][j][0] * table[i][j][1]
                    max_area = current_area if current_area > max_area else max_area
        pprint.pprint(table)
        return max_area

# this_matrix = [["1","0","1","0","0"], ["1","0","1","1","1"],
#   ["1","1","1","1","1"], ["1","0","0","1","0"]
# ]


# this_matrix = [["1", "1"]]
# this_matrix = [["1", "0"], ["1", "0"]]
this_matrix = [["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]
pprint.pprint(this_matrix)

print Solution().maximalRectangle(this_matrix)
