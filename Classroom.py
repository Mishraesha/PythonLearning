class Student:

    school = "Anthony"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2 = m2
        self.m3 = m3

    def avergae(self):
        return (self.m1+self.m2+self.m3)/3

class1=Student(23,44,12)
class2=Student(20,94,12)

print("Average of class1:",class1.avergae())
print("Average of class2:",class2.avergae())

