# Task-1 Check if a number is positive, negative, or zero.

# print('Task-1 Check if a number is positive, negative, or zero.')

# a =int(input("Enter Your Number:"))

# if(a==0):
#     print("Your Number Is 0")

# elif(a>0):
#     print("Your Number Is Positive")
# else:
#     print("Your Number Is Negative")


# Task-2 Check Your Number Is Even Or Odd
# print("Task-2 Check Your Number Is Even Or Odd.")

# Value = int(input("Enter Your Value:"))

# if (Value%2==0):
#     print("Your Number Is Even!!!")
# else:
#     print("Your Number Is Odd!!!")






# Task-3 Find the largest among three numbers.

# print("Task-3:Find the largest among three numbers.")

# number1=int(input("Enter Your First Number :"))
# number2=int(input("Enter Your Second Number :"))
# number3=int(input("Enter Your Third Number :"))

# if (number1 == number2 == number3):
#     print("You Enter Equal Same Number 3 times ",number3)

# elif(number1>number2 and number1>number3):
#     print(f"Your First Number {number1} Is Greater")

# elif(number2>number1 and number2>number3):
#     print(f"Your Second Number {number2} Is Greater")

# else:
#     print(f"Your Third Number {number3} Is Greater")



# Task 4 :Check whether a year is a leap year.

# Year=int(input("Enter Year:"))

# if (Year%4 ==0 and (Year%400==0 or Year%100 !=0)):
#     print(f"Your Year {Year} is Leap Year")

# else :
#     print("Year Is Not A Leap Year")






# Task-5 :Check if a character is a vowel or consonant.

# Character = input("Enter A Character:")
# if ('a'==Character  or 'e' ==Character or 'i' ==Character or 'o'==Character or  'u'==Character or 'A'==Character or 'I' ==Character or 'E' ==Character or  'O'==Character or 'U'==Character):
#     print("Your Letter Is Vowels")

# else:
#     print("Your Letter Is Consonant")



# Task-6 :Check if a person is eligible to vote.

# Age = int(input("Enter Your Age :"))
# if (Age<0):
#     print("Age Never be Negative!!!!")
#     print("Please EnterValid Age")
# elif (Age<18):
#     print("You Can't Vote Wait Few Year")
#     print("Thank You")
# else:
#     print("Your Can Vote")
#     print("Thank You")


# Task 7  Find grade based on percentage.
# percentage = int(input("Enter Your Percentage :"))

# if(percentage >100):
#     print("Invalid Percentage");
# elif(percentage >= 90 and percentage <100):
#     print("A++ Grade")
# elif(percentage >=75  and percentage <80):
#     print("A Grade")
# elif(percentage >= 60 and percentage <75):
#     print("B Grade")
# elif(percentage >= 45 and percentage <60):
#     print("C Grade") 
# elif(percentage > 33 and percentage <45):
#     print("D Grade")  
# else:
#     print("You Failed")



# Task-8 Check if a number is divisible by 5 and 11.

# number = int(input("Enter Your Number :"))

# if (number % 5 == 0 and number % 11== 0):
#     print("Your Number Is divisible By 5 and 11")

# else :
#     print("Your Number Is Not Divisible By 5 and 11")

# Task-9 Check if the angles form a valid triangle.

# Angel1 = int(input("Enter Your first Angel: "))
# Angel2 = int(input("Enter Your Second Angel: "))
# Angel3 = int(input("Enter Your Third Angel: "))

# if (Angel1 + Angel2 + Angel3 == 180):
#     print("Your Angels Are valid!!!")

# else:
#     print("Your Angel Are Invalid!!!")


#Task -10 Check if a number is an Armstrong number.Using While Loop;


# number = int(input("Enter The Value :"))

# count = len(str(number))
# print("count =",count)
# ans= 0;
# while(number != 0):
#     rem = number%10;
#     number = number//10;
#     ans = ans + (rem**count);

# print("The Value ",ans);

# Using For Loop

# number = int (input("Enter A Number : "))
# str_number = str(number)
# count = len(str_number)
# r= 0;
# for i in str_number:
#     r = r + (int(i) ** count);

# print(r);


# # Task-11 Check if a number is a multiple of 3 or 7.

# Number = int(input("Enter A Number :"))

# if (Number % 3 ==0 or Number % 7 == 0):
#     print("Yes Number Is Reminder Of 3 Or 7")
# else:
#     print("No is Not A Reminder Of 3 Or 7")



# Task-12 Find the type of triangle (Equilateral, Isosceles, Scalene).

# Side1 = int(input("Enter The Length Of First Side:"))
# Side2 = int(input("Enter The Length Of Second Side:"))
# Side3 = int(input("Enter The Length Of Third Side:"))

# if Side1 == Side2 == Side3:
#     print("Tri-Angle Is Equilateral")

# elif Side1 == Side2 != Side3 or Side1 != Side2 == Side3 or Side1 == Side3 !=Side2:
#     print ( "Tri-Angle Is Isosceles" )

# elif Side1 != Side2 != Side3:
#     print("Tri-Angle Is Scalene") 



# Task-13 Create a simple calculator using conditional statements.

# First = int(input("Enter A First Number:"))
# Second = int(input("Enter A Second Number:"))

# Operation = input("Choose Operation ( + , - , * ,/): ")

# if Operation == '+':
#     print("Your Answer Is :" ,First + Second)
# elif Operation =='-':
#     print("Your Answer Is :",First-Second)
# elif Operation =='*':
#     print("Your Answer Is :",First*Second)
# else:
#     print("Your Answer Is :",First/Second)


# Question 14. Check if a number is prime.

# Number = int(input("Enter A Number :"))

# if Number <0:
#     print("Negative Number Is Not A Prime Number")

# else:
#     for i in range (2,Number):
#         if Number % i == 0:
#             a = "Not A Prime Number!!!!"
#             break

#         else:
#             a= "Number Is Prime Number!!!!!"
# print(a)


# Question 15 Print day of the week based on a number (1–7).

# Day = (input("Enter A Number To Choose Day Between 0-7:"))

# if Day =='1':
#     print("You Choose Monday")

# elif Day == '2':
#     print("You Choose TuesDay")

# elif Day == '3':
#     print("You Choose WedNasDay")

# elif Day == '4':
#     print("You Choose ThursDay")

# elif Day == '5':
#     print("You Choose FriDay")

# elif Day == '6':
#     print("You Choose SaturDay")

# elif Day =='7':
#     print("You Choose Sunday")

# else:
#     print("Choose Between 1 - 7")



# Question 16 Check if a year is a century year.

# Year = int(input("Enter A Year To Check Century Year Or Not:"))

# if Year % 100 == 0:
#     print(Year , 'Is Century Year!!!')
# else:
#     print(Year , 'Is Not Century Year!!!')