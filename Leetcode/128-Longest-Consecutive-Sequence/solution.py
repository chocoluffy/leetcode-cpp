class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        def find(parent, idx):
            if parent[idx] != idx:
                parent[idx] = find(parent, parent[idx])
            return parent[idx]
        parent = {}
        rank = {}
        visited = {}
        for i in nums:
            parent[i] = i
            rank[i] = 1
            visited[i] = False
        for i in nums:
            if not visited[i]:
                visited[i] = True
                if (i+1) in parent: # reach boundary.
                    p = find(parent, i+1)
                    parent[i] = p
                    rank[p] += rank[i]
        return max([v for k, v in rank.iteritems()])