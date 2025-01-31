# Max Consecutive Ones III
# Soln: 36ms Runtime, beats 79.03%, 18.38MB memory, beats 30.98%

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                k -= 1
            j+=1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i