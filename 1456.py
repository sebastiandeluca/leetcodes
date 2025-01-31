# Maximum Number of Vowels in a Substring of Given Length
# Soln: 74ms Runtime, beats 72.35%, 18.04MB memory, beats 48.24%
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a','e','i','o','u'}
        count = sum(1 for i in s[:k] if i in vowels)
        maxC = count
        for i in range(n - k):
            if s[i] in vowels:
                count -= 1
            if s[i+k] in vowels:
                count += 1
            maxC = max(count, maxC)
        return maxC

                