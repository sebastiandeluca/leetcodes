# Move Zeroes
# Soln: 11ms Runtime, beats 38.72%, 13.78MB memory, beats 7.90%

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z = 0
        n = len(nums)
        for x in range(n):
            if nums[x] != 0:
                nums[x], nums[z] = nums[z], nums[x]
                z += 1
        return nums