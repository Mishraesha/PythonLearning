class classA:
    def __init__(self):
        print("Class A constructor")

    def method1(self):
        print("Class A - Method 1")


class classB():
    def __init__(self):
        #super().__init__()
        print("Class B constructor")

    def method2(self):
        print("Class B - Method 2")

class classC(classB, classA):
    def __init__(self):
        super().__init__()
        print("Multiple inheritance - Class c")

c1 = classC()


