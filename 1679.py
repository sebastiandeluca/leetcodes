# Max Number of K-Sum Pairs
# Soln: 590ms Runtime, beats 11.00%, 21.78MB memory, beats 75.81%

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        c = 0
        l, r = 0, n - 1

        while l < r:
            t = nums[l] + nums[r]

            if t == k:
                l += 1
                r -= 1
                c += 1
                print("gotteem")
            elif t > k:
                r -= 1
            else:
                l += 1
        return c

