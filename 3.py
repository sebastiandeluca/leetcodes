# Longest Substring without Repeating Characters
# Soln:29 ms Runtime, beats 38.76%, 13.18MB memory, beats 49.41%

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        maxLen = 0
        chars = set()
        l = 0

        for r in range(n):
            if s[r] not in chars:
                chars.add(s[r])
                maxLen = max(maxLen, r - l + 1)
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
        return maxLen
