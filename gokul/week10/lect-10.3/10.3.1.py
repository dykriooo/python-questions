# create a class student with two attributes name and roll number and one method called display that prints the roll and name of the student.

# create two objects of the class student and display the details of the students.


class student :
    def __init__(self,name,roll):
        self.name = name 
        self.roll = roll

    def display(self):
        print(self.name)
        print(self.roll)

    def display1():
        print("ghuig")
        

s1 = student("rio",1)
s2 = student("ganu",2)
s3 = student("rhfi",3)

# print(s1)
# print(s2)
# print(s3)

s1.display()
s2.display()
s3.display()

student.display1()