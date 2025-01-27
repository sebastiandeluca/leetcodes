# String Compressiom
# Soln: 3ms Runtime, beats 61.86%, 12.43MB memory, beats 66.44%
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ans = 0
        i = 0
        while i < len(chars):
            l = chars[i]
            count = 0
            while i < len(chars) and chars[i] == l:
                count += 1
                i += 1
            chars[ans] = l
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        return ans

# Soln: 4ms Runtime, beats 39.44%, 12.54MB memory, beats 38.60%

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = []
        completed = []
        n = len(chars)
        x = 0
        while x < n:
            count = 1
            z = 1
            while x + z < n and chars[x + z] == chars[x]:
                count += 1
                z += 1
            s.append(chars[x])
            
            if count > 1:
                s.extend(list(str(count)))

            x += z
            

        chars[:len(s)] = s
        return len(s)

