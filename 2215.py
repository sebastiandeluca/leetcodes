# Find the Difference of Two Arrays
# Soln: 3ms beats 94.64%, 12.86MB beats 22.62%
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        h1 = set(nums1)
        h2 = set(nums2)

        for num in nums2:
            if num in h1:
                h1.remove(num)
                h2.discard(num)

        return [list(h1), list(h2)]

# Soln: 471ms beats 23.27%, 12.69MB beats 83.75%
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        return [list(filter(lambda x: x not in nums2,dict.fromkeys(nums1))), list(filter(lambda x: x not in nums1, dict.fromkeys(nums2)))]
