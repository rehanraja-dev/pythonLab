class Demo:
    x = 10

    def __init__(self):
        self.y = 20
        self.z = 20
        Demo.a = 10

    def show(self):
        k = 10

d = Demo()

print(d.__dict__)
print(Demo.__dict__)