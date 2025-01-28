# Container with most water
# Soln: 123ms Runtime, beats 17.00%, 20.76MB memory, beats 40.62%

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        h = n - 1
        a = 0
        while l < h:
            c = (h - l) * min(height[l], height[h])
            a = max(a,c)
            if height[l] < height[h]:
                l += 1
            else:
                h-= 1
        return a
