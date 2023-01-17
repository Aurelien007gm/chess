class Move:

    def __init__(self,i,j,k,l,spec):
        self.i = i
        self.j = j
        self.k = k
        self.l =l
        self.spec = spec

    def show(self):
        print(self.i,self.j,self.k,self.l)
        print(self.spec)
        
    def equal(self,move):
        return(self.i == move.i and self.j == move.j and self.k == move.k and self.l == move.l and self.spec == move.spec)