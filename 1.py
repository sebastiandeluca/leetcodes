# Two Sum -- Easy
#Soln: 3ms Runtime, beats 62.89%, 13.30MB memory, beats 32.41% (2nd attempt, using hashmap)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        z = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in z:
                return [z[comp],i]
            z[nums[i]] = i
        return []

# Soln: 2069ms Runtime, beats 28.62%, 13.44MB memory, beats 10.83% (1st attempt, brute force)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)): # First integer
            for y in range(x + 1, len(nums)): # 2nd integer
                if nums[x] + nums[y] == target:
                    return [x, y] # Return indices if sum is target
        return [] # No soln found
    
# 



        