# Longest Increase Subsequence
# Soln: 4ms beats 97.16%, 12.68mb memory beats 80.48%

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = [nums[0]]
        for num in nums:
            i = bisect_left(sub,num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
