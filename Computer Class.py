#Class Definition
class Computer:
    #Initialising the variables - type of a constructor
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    #One method inside the class
    def config(self):
        print(self.cpu,self.ram)

#creating an instance of  class
Comp1 = Computer("i5","1TB")

print(Comp1.config())

