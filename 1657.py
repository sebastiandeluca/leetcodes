# Determine if Two Strings are Close
# Soln: 284ms 16.2MB

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        f1 = [0] * 26
        f2 = [0] * 26
        n = len(word1)
        if n != len(word2):
            return False
        for c in range(n):
            f1[ord(word1[c]) - ord('a')] += 1
            f2[ord(word2[c]) - ord('a')] += 1
        
        for i in range(26):
            if (f1[i] == 0 and f2[i] != 0) or (f1[i] != 0 and f2[i] == 0):
                return False
        
        f1.sort()
        f2.sort()

        for i in range(26):
            if f1[i] != f2[i]:
                return False
        return True