# Unique Number of Occurrences
# Soln: 0ms beats 100, 12.4MB beats 90.67%

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        n = len(arr)
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        freqs = set()
        for a,b in freq.items():
            freqs.add(b)
        return len(freqs) == len(freq)
