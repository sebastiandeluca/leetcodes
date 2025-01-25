# Asteroid Collision -- Medium
#Soln: 0ms Runtime, beats 100%, 13.43MB memory, beats 23.04%
class Solution(object):
    def asteroidCollision(self,asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        for a in asteroids:
            while res and a < 0 < res[-1]:
                if -a > res[-1]:
                    res.pop()
                    continue
                elif -a == res[-1]:
                    res.pop()
                break
            else:
                 res.append(a)
        return res