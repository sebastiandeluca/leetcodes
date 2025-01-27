# Can Place Flowers
# Soln: 7ms Runtime, beats 83.73%, 12.99MB memory, beats 60.47%

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowers = len(flowerbed)
        c = 0
        if flowers == 0 and n != 0:
            return False
        for x in range(0,flowers):
            if flowerbed[x] == 0:
                if x + 1 > flowers - 1:
                    if flowerbed[x-1] != 1:
                        c+= 1
                        flowerbed[x] = 1 # Modify array to account for sequential 0s
                elif x - 1 < 0:
                    if flowerbed[x + 1] != 1:
                        c += 1
                        flowerbed[x] = 1 # Modify array to account for sequential 0s
                else:
                    if flowerbed[x - 1] != 1 and flowerbed[x + 1] != 1:
                        c += 1
                        flowerbed[x] = 1 # Modify array to account for sequential 0s
        return c >= n

