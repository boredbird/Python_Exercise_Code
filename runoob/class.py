class a:
    def __init__(self):
        self.m = 1

    def add(self):
        self.p = 4
        print self.m + self.p

class b(a):
    def __init__(self):
        a.__init__(self)
        self.n = 2

    def sum(self):
        print self.m +self.n


c = b()
c.sum()
c.add()