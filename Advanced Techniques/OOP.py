class Student:
    def __init__(self,givenFirstName,givenSurname,GivenYear):
        self.__firstname = givenFirstName
        self.__surname = givenSurname          #Python does not encapsulate by default, to force it to put a double underline before the name
        self.year = GivenYear
        self.onRoll = True


    def getFirstName(self):
        return self.__firstname

    def setFirstName(self, newFirstName):
        if presencecheck(newFirstName):
            self.__firstname = newFirstName

def presencecheck(item):
    if item != "":
        return True
    return False

tyrone = Student("Tyrone","Vincent",11)

print(tyrone.onRoll)

print(tyrone.getFirstName())

tyrone.setFirstName("Stephan")

print(tyrone.getFirstName())

