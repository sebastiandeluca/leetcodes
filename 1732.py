# Find the Highest Altitude
# Soln: 0ms Runtime, beats 100.00%, 12.36MB memory, beats 70.53%

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currentAltitude = 0
        highest = currentAltitude
        for i in range(len(gain)):
            currentAltitude += gain[i]
            highest = max(highest, currentAltitude)
        return highest

