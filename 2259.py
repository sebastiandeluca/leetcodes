# Remove Digit From Number to Maximize Result -- Easy
# Soln: 0ms Runtime, beats 100%, 17.63MB memory, beats 48%

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        val = 0 # Sets up baseline for return value
        for x in range(len(number)):
            if number[x] == digit:
                check = int(number[:x] + number[x+1:]) # create int of string w/o the digit
                if check > val: # Compare to current highest found value
                    val = check
        return str(val)
