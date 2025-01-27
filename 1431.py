# Kids with the Greatest Number of Candies
# Soln: 0ms Runtime, beats 100.00%, 12.44MB memory, beats 40.14%

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # USE >=
        res = []
        n = len(candies)
        most_candies = max(candies)
        for kid in candies:
            if kid + extraCandies >= most_candies:
                res.append(True)
            else:
                res.append(False)
        return res

        
