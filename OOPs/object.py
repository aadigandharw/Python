# class spy ():
#     cname = "Python FullStac Dev"
#     tname = "Vinay"

# ob1 = spy()
# ob2 = spy()

# print(ob2.cname)



# Default Constructor 

# class a():
#     c = "vinay"
#     def __init__(self):
#         print("Constructor Called")
# ob1 = a()
# ob2 = a()


# Constructor 

# class spider ():
#     cname = " Python Full Stack"
#     def __init__(self,name,age,gender,mobileNo):
#         self.name = name
#         self.age = age 
#         self.gender = gender
#         self.mobileNo = mobileNo

# ob1 = spider("Ram",21,"male",91193783892)
# ob2 = spider("Madhu",22,"female",985559884545484)

# print(ob1.name,ob1.age,ob1.gender,ob1.mobileNo)

# print(ob2.name,ob2.age,ob2.gender,ob2.mobileNo)


# OBJECT METHOD


# Example.
# Bank Account Management Program

# class bank ():
#     Bankname = "SBI"
#     ROI = " 0.07"
#     def __init__(self,name,mobileNo,acnum,bal):
#         self.name = name
#         self.mobileNo = mobileNo
#         self.acnum = acnum
#         self.bal = bal

#     def checkbalance(self):
#         print(f"{self.name} Current Balance In Account Is {self.bal}")


#     def Deposit(self,amount):
#         self.bal += amount
#         print("Amount Deposit")

#     def Withdraw(self,amount):
#         if self.bal>amount:
#             self.bal -= amount
#             print("Amount WithDrawl")
#         else:
#             print("Insufficient Balance")


# ob1 = bank("Vinay",444984256485,16666666644,50000)

# ob1.checkbalance()
# ob1.Deposit(5000)
# ob1.Withdraw(15000)
# ob1.checkbalance()





# # CLASS METHOD 

# class bank ():
#     Bank_name = "HDFC_BANK"
#     ROI = 0.07

#     def __init__(self,name,mobn,accn,bal):
#         self.name = name 
#         self.mobn = mobn
#         self.accn = accn 
#         self.bal = bal 

#     @classmethod
#     def ChangeROI (cls,n):
#         cls.ROI = n

# ob1 = bank('amar',9879983282,55864645987,50000)
# ob2 = bank("hari",54444444444,4555555555,40000)
# ob3 = bank('Shiva',6555555555553,566666666,30000)
# ob4 = bank("vinay",66666666666,2888846565,20000)

# print("Before ROI VAlUES Is :")
# print(ob1.ROI,ob2.ROI,ob3.ROI,ob4.ROI)

# ob1.ChangeROI(0.09)

# print("After ROI VALUES IS:")
# print(ob1.ROI,ob2.ROI,ob3.ROI,ob4.ROI)



#Static Method

# class Bank():
#     Bank_Name= "RBI"
#     ROI = 0.09
#     def __init__(self,name,mbn,acc,bal,pin):
#         self.name = name
#         self.mbn = mbn
#         self.acc = acc
#         self.bal = bal 
#         self.pin = pin 
#     @classmethod
#     def ChangeROI(cls,n):
#         cls.ROI = n
#     def WithDraw (self):
#         if self.pin == self.getpin():
#             amount = int(input("Enter Amount:"))
#             if self.bal >= amount:
#                 self.bal -= amount
#                 print("Amount Debit Successful")
#             else:
#                 print("insufficient Balance")
#         else:
#             print("Incorrect Pin")
        
#     def CheckBalance(self):
#         if self.pin == self.getpin():
#             print (f"{self.name} Current Balance Is {self.bal}")
#         else:
#             print("Incorrect Pin")
#     @staticmethod
#     def getpin():
#         return int(input("Get Pin : "))
        
# ob1 = Bank("Vinay",84665948545,1555154545,50000,4444)

# ob1.CheckBalance()
# ob1.WithDraw()


# Getter + Setter  Method For Private VAriables 

class a():    
    def __init__(self):
        self.__x = 20
    def getter(self):
        return self.__x
    def setter(self,n):
        self.__x = n

ob = a()
print("Before Updating Private Variable!!!!")
print(ob.getter())
ob.setter(50)
print("After Updating Private Variable!!!!!")
print(ob.getter())



