# Reverse Words in a String
# Soln: 0ms Runtime, beats 100.00%, 12.76MB memory, beats 5.81% (Attempt 2)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def not_blank(a):
            if a != "" and a != " ":
                return a
        return " ".join(filter(not_blank,list(reversed(s.split(" ")))))
    

# Soln: 3ms Runtime, beats 43.37%, 12.51MB memory, beats 49.85% (Attempt 1)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def not_blank(a):
            if a != "" and a != " ":
                return a
        l = list(reversed(s.split(" ")))
        x = filter(not_blank, l)
        return " ".join(x)