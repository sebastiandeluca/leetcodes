# Greatest Common Divisor of Strings -- Easy
# Soln: 0ms Runtime, beats 100%, 12.52MB memory, beats 13.90%

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1+str2 != str2+str1:
            return "" # Strings have no GCD
        if len(str1) == len(str2):
            return str1 # Strings are the same
        
        # Recursively run gcdOfStrings until a GCD is found
        if len(str1)> len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1,str2[len(str1):])            


