# Nth Digit
# Soln: 0ms beats 100%, 12.45MB beats 38.71%
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = base = 1 # starting from 1 digit
        while n > 9*base*digit: # upper limit of d digits 
            
            n -= 9*base*digit
            digit += 1
            base *= 10 
            print(n,digit,base,9*base*digit)
        q, r = divmod(n-1, digit)
        return int(str(base + q)[r])

# Soln: 0ms beats 100%, 12.52MB beats 10.75%
    class Solution(object):
        def findNthDigit(self, n):
            """
            :type n: int
            :rtype: int
            """
            start, size, step = 1, 1, 9
            while n > size * step:
                n, size, step, start = n - (size*step), size+1, step *10, start * 10
            return int(str(start + (n - 1) // size)[(n - 1) % size])