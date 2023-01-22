## Num class Summarizes a stram of numbers
class Num:
    
    ## constructor created for Num class
    def __init__(self, at = 0, txt = ""):
        self.at = at
        self.txt = txt

        self.n = 0
        self.mu = 0
        self.m2 = 0

        self.lo = float('inf')
        self.hi = float('-inf')

        self.w = -1 if '-$' in txt else 1

    ## add method adds the n value also,
    ## It upadtes the values of lo,hi d, mu,m2 which is used for,
    ## calculating standard devaiation. 
    def add(self, value: float):
        self.n = self.n + 1
        d = value - self.mu
        self.mu = self.mu + (d / self.n)
        self.m2 = self.m2 + (d * (value - self.mu))
        self.lo = min(value, self.lo)
        self.hi = max(value, self.hi)

    ## mid method return the mean. 
    def mid(self):
        return self.mu

    # div method uses Welford's algorithmn to calculate standard deviation,
    # here is the link for Welford's algorithmn http://t.ly/nn_W
    def div(self): 
        if((self.m2 < 0) or (self.n < 2)):
            return 0
        return pow((self.m2 / (self.n - 1)), 0.5)
