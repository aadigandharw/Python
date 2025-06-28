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
# str_1 = list(str_1) n

# count = len(str_1)
# str_2 = list()

# j=count-1;

# for i in range(0 , count):
#     str_2 = str_1[j]
#     print(str(str_2),end="")
#     j=j-1

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
# list2 = []


# for i in list1:
#     if i not in list2:
#         list2.append(i)

# print(list2)

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

# number = list(input("Enter Numbers:"))
# ans=0
# print(number)

# for i in number:
#     ans = ans+int(i);

# print("Sum Of digits Is ",ans)



# Question 12. Print a pattern using nested loops (e.g., triangle of stars).

# Star = int(input("Enter A Number :"))

# for i in range(1,Star+1):
#     for j in range(1 ,i+1):
#         print("*" ,end= " ")
#     print()



# Question No. 13. Find the factorial of a number using a for loop.

# n = int (input("Enter Your Number:"))

# if(n == 0):
#     print(f"factorial of {n} is  1 ")
# else:
#     ans = 1
#     for i in range(1,n+1):
#         ans= ans * i
#         print("Your Factorial is ",ans)


# Question No- 14. Check if two strings are anagrams.

# A = input("Enter A First String:")
# B = input("Enter A Second String:")
# Len_A = len(A)
# Len_B = len(B)
# C = ""

# if(Len_A != Len_B):
#     print("Not A Anagrams")

# else:
#     for i in range(0,Len_A):
#         for j in range(0,Len_B):
#             if A[i] == B[j]:
#                 C = C + A[i]
#     if A == C:
#         print("String Is Anagrams")
#     else:
#         print("String Is Not A Anagrams")

# Question-15 Find common elements in two lists.
    
# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [5,3,12,34,2,0]

# l3 = []

# for i in l1:
#     for j in l2:
#         if i == j:
#             l3.append(i)
# print(l3)

# Question 16. Check if a year is a leap year.

# Year = int(input("Enter A Year To Check: "))

# if Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0):
#     print (Year ,"Is A Leap Year")
# else:
#     print("Not A Leap Year")

# Question 17. Find the largest of three numbers.

# a = int(input("Enter A First Number:"))
# b = int(input("Enter A Second Number:"))
# c = int(input("Enter A Third Number:"))

# if (a>b and a>c):
#     print(a , "Is Greater Than All Of These")
# elif b>a and b>c :
#     print(b , "Is Grater Than All Of These")
# else:
#     print(c,"Is Greater Than All Of This")


# Question 18. Create a dictionary from two lists.

# l1 = [ "name" , 'rollNo.' , 'age']
# l2 = ["Ram",'12','22']
# count_l1 = len(l1)
# count_l2 = len(l2)
# d = {}

# if count_l1 != count_l2:
#     print("No. Of element Need To Be Same")

# else:
#     for i in range(0,count_l2):
#         d[l1[i]] = l2[i]
#         print(d)




# Question 19. Convert Celsius to Fahrenheit.

# Celsius = int(input("Enter A Temperature in Celsius: "))

# Fahrenheit  = Celsius * (9/5)+32

# print(Fahrenheit)



#Question 20. Check if all elements in a list are even.

# l = [20,40,50,10,12]

# for i in l:
#     if i % 2 != 0:
#         a = "All Are Not Even!!!"
#         break
#     else:
#         a = "All Are Even!!!"
# print(a)

# Question 21. Find the second largest number in a list.

# l = [10,20,11,40,15,14,71,12,13,50,71]

# l.sort(reverse=True)
# l = set(l)
# print(l[1])
# count = len(l)
# for i in range(0,count):
#     if i == 1:
#         print(l[i],"Is The Second Largest Number")
#         break


# Question 22. Sort a list without using built-in sort method. Nahiiiii Banaaaaa haaiiiii

# l1 = [10,20,11,40,15,14,71,12,13,50]
# len_l1 = len(l1)
# l2 = []
# for i in range (0,len_l1):
#     for j in range (0,len_l1):

#         if l1[i] > l1[j]:
#             l1[i] ,l1[j] = l1[j] , l1[i]


# print(l2)

# Question 23. Count how many times an element appears in a list.

l1 = [10,20,11,40,15,14,71,12,13,50]
length = len(l1)
count =0

Element = int(input("Enter A Element That You Want To Check:"))

for i in range (0,length):
    if Element == l1[i]:
        count = count+1

print(f"{Element} is  {count} time In List")


# Question 24 merge two dictionaries.















