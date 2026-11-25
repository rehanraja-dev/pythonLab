class DemoMath:
    @staticmethod
    def add(x,y):
        print("The sum: ", x+y)
    
    @staticmethod
    def product(x,y):
        print("The product: ", x*y)

    @staticmethod
    def average(x,y):
        print("The avg: ", (x+y)/2)

DemoMath.add(2,3)
DemoMath.product(2,3)
DemoMath.average(2,3)