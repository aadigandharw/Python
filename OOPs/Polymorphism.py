# class Sample():
#     def sum (a,b):
#         return a+b
#     def sum(c,d,e):
#         return c+d+e
#     def sum(f,g,h,i):
#         return f+g+h+i

# Object = Sample()

# print("Sum Of Number Is :",Object.sum(2,3,4,6))

# print( "Sum Of Number IS:",Object.sum(2,3,4))

# print( "Sum Of Number IS:",Object.sum(2,3,4,5))


# 1. Compile Time Polymorphism (Method Over Loadind)

# class Sample():
#     def sum(self, *args):
#         return sum(args)

# # Create object
# obj = Sample()

# # Function calls with different number of arguments
# print("Sum Of Number Is:", obj.sum(2, 3))           # Output: 5
# print("Sum Of Number Is:", obj.sum(2, 3, 4))        # Output: 9
# print("Sum Of Number Is:", obj.sum(2, 3, 4, 5))     # Output: 14



# 2 . Run Time Polymorphism 

# class Animal():
#     def speak(self):
#         print("Animal Make's A Sound")
    
# class Dog(Animal):
#     def speak(self):
#         print("Dog Barks")

# class Cat (Animal):
#     print("Cat Meow's")

# # Function That Accept Any Animal
# def make_sound(animal):
#     animal.speak()

# make_sound(Animal())
# make_sound(Dog())
# make_sound(Cat())


# class Animal():
#     a= 10
#     print(a)
#     print("Class Makes A Sound")
#     def sum(self):
#         print("Hello")

# Animal().sum()

class MyClass:
    def hello(self):
        print("Hello")

MyClass().hello()
