import math

## Summarizes a stream of symbols
class Sym:

    ## Constructs the SYM class
    def __init__(self, at = 0, txt = ""):
        self.at = at
        self.txt = txt

        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    ## add function updates the counts for the values that has been seen so far
    ## it doesn't return any value
    def add(self, x: chr):
        self.n = self.n + 1
        if x in self.has:
            self.has[x] = self.has[x] + 1
        else:
            self.has[x] = 1
        
        if self.has[x] > self.most:
            self.most = self.has[x]
            self.mode = x
    
    ## Mid method returns the mode (most frequent)
    def mid(self):
        return self.mode

    ## div method returns the entropy 
    def div(self):
        e = 0
        for i in self.has:
            p = self.has[i] / self.n
            e = e + (p * math.log(p, 2))
        return -e


