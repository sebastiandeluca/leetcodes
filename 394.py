# Decode String -- Medium
# Soln: 0ms Runtime, beats 100.00%, 12.49MB memory, beats 35.95%

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        n = 0
        t = ""
        for i in s:
            if i.isdigit():
                n = (n * 10) + int(i)
            elif i == "[":
                res.append((t,n))
                n = 0
                t = ""
            elif i == ']':
                string,nums = res.pop()
                t = string + (t * nums)
            else:
                t += i
        return t
        