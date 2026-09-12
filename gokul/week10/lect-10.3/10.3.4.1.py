class Student:
    def __init__(self,naam:str,serial:int,dob="19081998"):
        self.Name=str (naam)
        self.Roll=int(serial)
        dob=dob


    def display(self):
        print(self.Roll,self.Name)

obj1=Student(1,"Gokul")
obj1.display() #gokul 1 

obj2=Student(Name="aswin")
# obj2.display() none aswin 

obj3=Student("Gokul")
obj3.display() # none gokul

# obj4=Student(Roll=13)
# obj4.display() #error 


s1=Student("gokul",1)
s1.display ()