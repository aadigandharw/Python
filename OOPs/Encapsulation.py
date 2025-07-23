class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age 
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age > 0 :
            self.__age = age
        
# Creating an object

s1 = Student("Aaduuuuu",20)

print(s1.name)
print(s1.get_age())

s1.set_age(50)
print(s1.get_age())