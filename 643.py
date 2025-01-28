# Maximum Average Subarray I
# Soln: 44ms Runtime, beats 95.00%, 19.14MB memory, beats 32.07%

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        w_sum = max_sum = sum(nums[:k])
        for i in range(n-k):
            w_sum = w_sum - nums[i] + nums[i+k]
            if w_sum > max_sum:
                max_sum = w_sum
        return max_sum/float(k)
                