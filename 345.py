# Reverse Vowels of a String\
# Soln: 324ms Runtime, beats 18.05%, 17.11MB memory, beats 9.06% (Attempt 1)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        v = []
        n = len(s)
        for x in range(n):
            if s[x] in vowels:
                v.append(s[x])
        
        spot = 0
        rv = list(reversed(v))
        n_s = ''
        for x in range(n):
            if s[x] in vowels:
                n_s += rv[spot]
                spot += 1
            else:
                n_s += s[x]
        return n_s