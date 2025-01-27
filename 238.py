# Product of Array Except Self
# Soln: 19ms Runtime, beats 98.67%, 19.89MB memory, beats 92.55%

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        z_c = 0
        n = len(nums)
        res = [0] * n

        for num in nums:
            if num == 0:
                z_c += 1
            else:
                p *= num
        if z_c > 1:
            return res # > 1 0 means all res will be 0
        if z_c == 1:
            for i in range(n):
                if nums[i] == 0:
                    res[i] = p
        else:
            for i in range(n):
                res[i] = p // nums[i]

        return res