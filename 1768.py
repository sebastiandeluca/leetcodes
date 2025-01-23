# Merge Strings Alternately -- Easy
# Soln: 11ms RUntime, beats 88.79%, 12.58MB memory, beats 8.58%
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length = 0 # baseline for length
        res = '' # Running total for result
        
        # Get the shortest word
        if len(word1)<len(word2):
            length = len(word1)
        else:
            length = len(word2)
        
        for x in range(0,length):
            # Add chars from each string, one at a time
            res += word1[x]
            res += word2[x]
        res += word1[length:len(word1)+1] # Add remainder of whichever word was longer
        res += word2[length:len(word2)+1]
        return res