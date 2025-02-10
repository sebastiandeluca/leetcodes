# Clear Digits
# beats 100%

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for char in s:
            if char.isdigit() and res:
                res.pop()
            else:
                res.append(char)
        return "".join(res)
