"""
- Construct a matrix by a bottom-up fashion, each entry record (m, n), meaning
  the consecutive 1s in two directions as bottom and right. Such as at position
  (i, j), there are m consecutive 1s from current position towards the bottom,
  and n such consecutive 1s towards the right. 

- then one more pass to find out the maximum area from the matrix entry.


# challenge:
- inner list being updated at the same time. but not individually! mind such
  reference error.
"""
import pprint
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]] :rtype: int
        """
        if not matrix:
            return 0
        table = [[(0, 0)] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
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
                validator = (table[i][j+1][0], table[i+1][j][1])
                if table[i][j][0] <= validator[0] and table[i][j][1] <= validator[1]:
                    current_area = table[i][j][0] * table[i][j][1]
                    max_area = current_area if current_area > max_area else max_area
        # pprint.pprint(table)
        return max_area

this_matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print Solution().maximalRectangle(this_matrix)