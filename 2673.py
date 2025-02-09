# Make Costs of Paths Equal in Binary Tree
# Soln: 139ms, beats 90.48%, 17.86MB, beats 95.24%

class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        ans = 0
        i = ((n + 1) / 2) - 2
        while i >= 0:
            ans += abs(cost[2*i+1] - cost[2*i+2])
            cost[i] += max(cost[2*i+1], cost[2*i+2])
            i -= 1
        return ans
