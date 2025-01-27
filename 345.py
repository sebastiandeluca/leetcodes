# Reverse Vowels of a String\
# Soln: 19ms Runtime, beats 69.94%, 13.86MB memory, beats 38.58%
class Solution(object):
    def reverseVowels(self, s):
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        
        while start < end:
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        
        return "".join(word)


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