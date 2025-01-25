# Dota2 Senate
# Soln: 1065ms runtime, beats 9.56%, 12.99MB memory, beats 18.24%

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        from collections import deque
        radiant = deque()
        dire = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r = radiant.popleft()
            print('r',r)
            d = dire.popleft()
            print('d',d)
            if r < d:
                radiant.append(r+n)
            else:
                dire.append(d+n)
        return "Radiant" if radiant else "Dire"