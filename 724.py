# Find Pivot Index
# Soln: 0ms, beats 100%, 13.15MB, beats 90.29%
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, sum(nums)
        for idx, ele in enumerate(nums):
            r -= ele
            if l == r:
                return idx
            l += ele
        return -1


# Soln: 3100ms, beats 14.83%, 13.30MB, beats 51.78%

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        c = -1
        for x in range(n):
            if sum(nums[:x]) == sum(nums[x+1:]):
                return x
        return c
