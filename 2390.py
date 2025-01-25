# Removing Stars from a String
#Soln: 291ms Runtime, beats 45.57%, 13.90MB memory, beats 72.31%
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s:
            # Treat string like a stack
            if i=='*':
                # Remove newest char from stack
                res.pop()
            else:
                # Add chars to stack
                res +=[i]
        return "".join(res) # return as string