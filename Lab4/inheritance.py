class Base:
    def __init__(self, a , b):
        self.x = a
        self.y = b

    def showBase(self):
        print(self.x, self.y)

class Derived(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.z = c

    def showDerived(self):
        print(self.z)

d1 = Derived(1,2,3)
d1.showBase()
d1.showDerived()