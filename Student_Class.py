#creating student class
class Student:
    def __init__(self, name, roll_number, marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def get_details(self):
        print(self.name)
        print(self.roll_number)
        print(self.marks)
    def is_passed(self):
        if self.marks > 30:
            return "Passed"
        else:
            return "Failed"
s1=Student("Name=Ram sharma", 102, 70)
s1.get_details()
print("Result",s1.is_passed())

s2=Student("Name=Sourabh sharma", 103, 30)
s2.get_details()
print("Result",s2.is_passed())