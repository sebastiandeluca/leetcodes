# Increasing Triplet Subsequence
# Soln: 27ms Runtime, beats 52.54%, 24.48MB memory, beats 40.08%

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f,s = float('inf'), float('inf')
        for x in nums:
            if x <= f:
                f = x
            elif x <= s:
                s = x
            else:
                return True
        return False
            

        
