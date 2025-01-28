# Is Subsequence
# Soln: 0ms Runtime, beats 100.00%, 12.86MB memory, beats 13.91%
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = 0
        n = len(t)
        for x in range(n):
            if l < len(s) and t[x] == s[l]:
                l += 1
        return l >= len(s)
    # Realized we don't return the subsequence, no point in swapping things!


# Soln: 330ms Runtime, beats 5.60%, 13.06MB memory, beats 9.39% (Attempt 1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = 0
        n = len(t)
        t = list(t)
        b = False
        for x in range(n):
            if l < len(s) and t[x] == s[l]:
                t[x], t[l] = t[l], t[x]
                print(s[l],l,t)
                l += 1
        if l < len(s):
            b = False # Case where s in t but not as a subsequence
        else:
            b = s in "".join(t) # Normal result
        return b
        