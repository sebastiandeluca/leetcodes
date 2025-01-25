# Number of recent calls
#Soln: 58 ms runtime, beats 80.67%, 17.51MB memory, beats 10.35%
class RecentCounter(object):

    def __init__(self):
        self.requests = [] # Initiate empty requests
        self.start = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1
        return len(self.requests) - self.start



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)