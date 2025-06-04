class Student:

    def __init__(self):
        self.firstname = "None"
        self.lastname = "None"
        self.age = "None"


mystudent = Student()

mystudent.firstname = "Yo"
mystudent.lastname = "Gurt"
mystudent.age = 47

print(mystudent.age)

students= [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student()

]