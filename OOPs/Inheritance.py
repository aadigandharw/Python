# class parent ():
#     def method1(self):
#         print("M1 Of Parent Class")
#     def method2(self):
#         print("M2 Of Parent Class")
# class Child(parent):
#     def method1(self):
#         print("M1 Of Child Class")

# object = Child()

# # Access By Object
# object.method1()
# object.method2()

# #Access By Class By Passing Instance Object
# Child.method1(object)
# Child.method2(object)


# a = "Aditya"
# s = []
# len = len(a)
# a = list(a)
# for i in range (len):
#     s.append(a[len-1-i])

# print("String",a)
# print("Reverse String",str(s))


# 2 Multi-Level Inheritance :----
# class bank1():
#     def __init__(self, name, mbn, acn, bal):
#         self.name = name 
#         self.mbn = mbn 
#         self.acn = acn 
#         self.bal = bal 

#     def details(self):
#         print(f'Name: {self.name}')
#         print(f'Mobile No: {self.mbn}')
#         print(f'Account Number: {self.acn}')
#         print(f'Balance: {self.bal}')

# class bank2(bank1):
#     def __init__(self, name, mbn, acn, bal, aadhar, mail):
#         super().__init__(name, mbn, acn, bal)
#         self.aadhar = aadhar
#         self.mail = mail 

#     def details(self):
#         super().details()
#         print(f'Mail: {self.mail}')
#         print(f'Aadhar: {self.aadhar}')

# class bank3(bank2):
#     def __init__(self, name, mbn, acn, bal, aadhar, mail, pan):
#         super().__init__(name, mbn, acn, bal, aadhar, mail)
#         self.pan = pan

#     def details(self):
#         super().details()
#         print(f'PAN ID: {self.pan}')

# # Create object and call method
# Ob = bank3('Vinay', 9133119, 98344499489, 500000, 28586079397, 'vinay@123', 'JJPJ12435')
# Ob.details()


# 3 Multiple Inheritance

# class Parent1 ():
#     def __init__(self):
#         print("Constructor Of Class Parent1")
# class Parent2 ():
#     def __init__(self):
#         print("Constructor Of Class Parent2")
# class Child(Parent1,Parent2):
#     def __init__(self):
#         Parent1.__init__(self)
#         Parent2.__init__(self)
#         print("Constructor Of Child Class")

# Obj = Child()

# 4 Hirarichal Inheritance 

# class a():
#     x = 100 
# class b (a):
#     z = 100 
#     y = 200 
# class c(a):
#     pass

# obj = c()
# print(obj.x)

# ob1 = b()
# print(ob1.x)


# 5 Hybrid Inheritance 

# class a ():
#     x = 100 
# class b (a):
#     z = 100 
# class c (a):
#     d = 100
# class d (b,c):
#     pass
# obj  = d()
# print(obj.x)