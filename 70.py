# Climbing Stairs
# Soln: 0ms Runtime, beats 100%, 17.97MB memory, beats 16.69%
#(I think runtime on leetcode might be glitching)

class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3: # when n <=3, # steps = n, so just return n
            return n
        p1 = 3
        p2 = 2
        c = 0
        for s in range(3,n): # build a fibonacci sequence
            c = p1+p2
            p2 = p1
            p1 = c
        return c