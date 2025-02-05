# Longest SubArray of 1's After Deleting One ELement
# Soln: 92ms runtime, beats 24.21%, 16.84mb memory, beats 40.95%

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        z = 0
        ans = 0

        for r in range(n):
            if nums[r] == 0:
                z += 1
            
            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1
            
            ans = max(ans, r - l + 1 - z)
        
        return ans - 1 if ans == n else ans