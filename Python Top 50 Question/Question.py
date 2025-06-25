# Top 50 Python Coding Questions

# Question:1 Check if a person is eligible to vote.

# Age = int(input("Enter Your Age"));
# if Age <0:
#     print ("Age Never Be Negative")
#     print ("Please Enter A Valid Age")

# elif (Age>=1 and Age < 18):
#     print ("Yor Are Not eligible")
#     print("Wait Few Year")
# else:
#     print ("You Can Vote!!!")


# Question:2 Count vowels in a string using a for loop.

# Str_1 = (input("Enter Your String:")
# Str_1 = Str_1.lower()

# count = 0;
# for i in Str_1:
#     if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
#         count=count+1;

# print("Number of Vowels in string",count)

# Question 3. Reverse a string without using built-in reverse function.

# str_1 = input("Enter A String: ")
# str_1 = list(str_1)

# count = len(str_1)
# str_2 = list()

# j=count-1;

# for i in range(0 , count):
#     str_2 = str_1[j]
#     print(str(str_2),end="")
#     j=j-1;

# Question-4. Find the maximum number in a list using a for loop.

# list1 = [20,5,50,100,60,80,101,10,1]
# list1.sort()

# a =0;
# for i in list1:
#     a = i;
# print("Maximum Element Of List Is :",a)

# Question 5. Check if a number is even or odd.

# number = int(input("Enter Your Number :"))

# if number % 2== 0 :
#     print (f"{number} is Even!!")
# else:
#     print(f"{number} is Odd!!")

# Question 6. Print all even numbers from 1 to 50.

# for i in range(2,51,2):
#     print(i,"Is Even");

# 7. Count frequency of characters in a string.

# str_1 = input("Enter A String:")
# print(f"Your String Is {str_1} Remember ")
# str_1 = str_1.lower()

# character = input("Enter A Character:")
# character = character.lower();
# count = 0

# for i in str_1:
#     if i == character:
#         count =count+1;
# print(f"Frequency Of {character} Is ",count)

# Question-8: Check if a number is prime.

# number = int (input("Enter A Number :"))


# if(number<0):
#     print("Negative Number Is Not A Prime Number")

# else:
#     for i in range (2,number):
#         k = number;
#         if k % i ==0:
#             print (f"{number}Not A Prime Number")
#             break
#         else:
#             print(f"{number} Is A Prime Number")
#             break
        
    

# Question 9 Remove duplicates from a list.

# list1 = [1,11,2,10,20,5,50,20,5,1]
# j=0

# for i in list1:
#     j=j+1
#     for j in list1:
#         if i == j:
#             list1.remove(j);
# print(list1);

# Question 10 Check if a string is a palindrome.

# String = input ("Enter A String :")
# String = String.lower()
# String = list(String)

# String_1 = list(reversed(String))



# if (String == String_1):
#     print("String Is Palindrome")
# else :
#     print ("String Is Not A Palindrome")


# question 11 Find the sum of digits of a number.

# num1 = int(input('Enter A First Number:'))
# num2 = int (input('Enter A Second Number:'))
# Sum = num1 + num2

# print(f"Sum =",Sum)

# Question 12. Print a pattern using nested loops (e.g., triangle of stars).

# Star = int(input("Enter A Number :"))
# Star = Star + 2
# j=0

# for i in range(1,Star):
#     for j in range(1 ,i):
#         print("*" ,end=" ")
#     print()
    
    

#Question No. 13. Find the factorial of a number using a for loop.

# number = int ( input("Enter A Number To Find A factorial :"))

# number = number+1







