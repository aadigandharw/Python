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

# elif number ==1:
#     print("Number Is Not A Prime Number")

# else:
#     for i in range (2,number):
#         k = number;
#         if k % i ==0:
#             print (f"{number} Is Not A Prime Number")
#             break
#     else:
#         print(f"{number} Is A Prime Number")
            
        
    

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
# print("Your Factorial is ",ans)


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

# for i in range(len_l1):
#     for j in range (1,len_l1):
#         if l1[i] > l1[j]:
#             l2.append(l1[j])
#             break
            
#         else:
#             l2.append(l1[i])
#             break
# print(l1)


# print(l2)

# Question 23. Count how many times an element appears in a list.

# l1 = [10,20,11,40,15,14,71,12,13,50]
# length = len(l1)
# count =0

# Element = int(input("Enter A Element That You Want To Check:"))

# for i in range (0,length):
#     if Element == l1[i]:
#         count = count+1

# print(f"{Element} is  {count} time In List")


# Question 24 merge two dictionaries.

# dic_1 = {1:'a',2:'b'}

# dic_2 = {3:'c',4:'d'}

# dic_1.update(dic_2)

# print("Merge Dictionary Is ",dic_1)


# Question 25. Find the length of a string without using len().

# str1 = "Vikash Yadusir"

# str1 = str1.lower()
# count=0

# for i in str1:
#     count = count+1
# print ("Length Of The String Is" , count)


# Question 26. Replace all spaces in a string with hyphens.

# str1 = "Vikash  sir Python Ki Class loh"

# str1 = str1.replace(" ","-")

# print(str1)


#Question  27. Find the smallest number in a list.

# l1 = [10,20,2,11,40,15,14,71,12,13,50]

# l1.sort()

# print("Smallest Number Is :",l1[0])

# Question 28. Check if a number is a perfect square.

# number = int(input("Enter A Number: "))

# for i in range(number):
#     if i*i == number:
#         a = "Is Perfect Square!!!"
#         break
#     else:
#         a = "Is Not Perfect Square!!!"

# print(number,a)

# Question 29. Find the sum of all even numbers in a list.

# l1 = [10,20,2,11,40,15,14,71,12,13,50]
# sum1=0

# for i in l1:
#     if i%2==0:
#         sum1 = sum1+i
# print("Sum Of All Even Number Is:" , sum1)


# Question 30. Find the product of all numbers in a list.

# l1 = [10,20,2,11,40,15,14,71,12,13,50]

# sum1=1

# for i in l1:
    
#         sum1 = sum1*i
# print("Product Of All Numbers In A list:" , sum1)

# Question 31. Swap two variables without using a third variable.

# a = int(input("Enter Your First Number:"))
# b = int(input("Enter Your Second Number:"))

# print("Before Swap!!!")
# print("Your First Number is :",a)
# print("Your Second Number is :",b)

# a , b = b , a

# print("After Swap!!!")
# print("Your First Number is :",a)
# print("Your Second Number is :",b)

# # Question 32. Print Fibonacci series up to n terms. Nahiiiii Bnaaaaa 

# Sequence = int(input("Enter A Number :"))

# f0 = 0
# f1 = 1
# n = 0

# for i in range(Sequence):
#     n = (f0-1)+(f1-2)
#     print(n)

# Question 33. Find the GCD of two numbers. 

# Yeh Question Nahi Bnaaaaaaa


# Question 34. Count the number of words in a string.

# str1 = "Vikash  sir Python Ki Class lohh"

# length = len(str1)

# for i in str1:
#     if i == " ":
#         length = length-1
    
# print("Number Of Words In String Is:",length)

# Question 35. Extract all digits from a string.


# str1 = "Vikash 5sir 4Pyth1on Ki 6Cl8as7s lohh"

# str2 = []
# for i in str1:
#     if i == "0" or i =="1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
#         str2.append(i)

# print("All Digit From A String Is:",str2)



# Question 36. Remove all vowels from a string.

# str1 = "Vikash 5sir 4Pyth1on Ki 6Cl8as7s lohh"

# str1 = str1.lower()

# list1 = list(str1)

# for i in list1:

#     if i == 'a' or i == 'e' or i == 'i' or i=='o' or i =='u':
#         list1.remove(i)

# list1 = str(list1)

# print((list1))


# Question 37. Print numbers divisible by 3 and 5 between 1 to 100

# for i in range(1,101):
#     if i % 3 ==0 and i % 5 == 0:
#         print ("Number Which Is Divisible by 3 and 5 is :",i)


# Question 38. Convert a number into binary without using bin()

# Number = int (input("Enter A Number :"))

# rem = 0 
# l1 = []

# while(Number):
#     rem = Number%2
#     Number = Number //2
#     l1.append(rem)

# count = len(l1)

# l2 =[]

# for i in range(count):
#     l2.append(l1[(count-1)-i])


# print(l2)



# Question 39. Reverse a list using a for loop.

# l1 = [10,20,2,11,40,15,14,71,12,13,50]

# l2 = []

# length = len(l1)-1

# for i in range(length+1):

#     l2.append(l1[length])
#     length=length-1

# print(l2)


# Question 40: Find the most frequent element in a list.

# l1 = [10,20,2,11,40,15,14,71,12,13,50,10,10] 

# element = int(input("Enter A Element To Find Frequency in List:"))
# frequency = 0

# for i in l1:
#     if i == element:
#         frequency = frequency +1

# print("Frequency In Element Is :",frequency)


# Question 41. Find all prime numbers in a given range. Question This Sehhhh Nahiii Bnaaaaa Bhaiiiii


# number = int (input("Enter A Range To Get All Prime Number: "))

# if number < 0:
#     print("Negative Number Is Not A Prime Number!!!!")
# else:
#     for i in range(2,number+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#             else:
#                 print(i)
#                 break
            



# Question 42. Print the multiplication table of a number

# Number = int(input("Enter A Number :"))

# for i in range(1,11):
#     print(i*Number)

# Question 43. Check if a list is sorted or not.


# l1 = [10,11,13,14,20,26,32,72,50,]

# length = len(l1)

# for i in range(length-1):
    
#     if l1[i] <= l1[i+1]:
#         a = "List Is Sorted"
#     else:
#         a = "List Is Not Sorted"
#         break
# print(a)


# Question 44. Create a list of squares from 1 to n.

# number = int(input("Enter A Number:"))

# l1 =[]

# for i in range(1,number+1):
#     print(i**2)



# 45. Find all palindromes in a list of strings.  Question Thik Seh Nahi Bnaaaa


# str1 = "Navin"

# count= len(str1)
# list1 = list(str1)
# list2 = []


# str1 = str1.lower()

# for i in list1:
#     list2 = 


# Question 46. Count how many uppercase and lowercase letters in a string.



# str1 = "Vikash  sir Python Ki Class lohh"

# upper = 0 
# lower = 0
# a,b = 0,0

# for i in str1:
#     if i =='a' or i =='b' or i =='c' or i =='d' or i =='e' or i =='f' or i =="g" or i=="h" or i =='i' or i =='j' or i =='k' or i =='l' or i =='m' or i =='n' or i =='o' or i =='p' or i =='q' or i =='r' or i =='s' or i =='t' or i =='u' or i =='v' or i =='w' or i =='x' or i =='y' or i =='z' :
#         a = a+1

#     elif i =='A' or i =='B' or i =='C' or i =='D' or i =='E' or i =='F' or i =='G' or i =='H' or i =='I' or i =='J' or i =='K' or i =='L' or i =='M' or i =='N' or i =='O' or i =='P' or i =='Q' or i =='R' or i =='S' or i =='T' or i =='U' or i =='V' or i =='W' or i =='X' or i =='Y' or i =='Z' :
#         b = b +1

# print(f"Lower Case in A String is {a} & Upper Case In A String {b} ")






# Question 47. Remove punctuation from a string Thik Seh Nahi Bna Hai

# str1 = "vikash ./';:'';,#/*/^&*($#*@#!!!)sir Python Ki Class loh"
# str1=list(str1)

# for i in str1:
#     if i=="." or i == "/" or i=="!" or i ==";" or i==":" or i == "(" or i==")" or i =="@" or i =="#" or i =="*" or i=="$" or i=="&" or i=="v" or i =="i" or i == ' ' :
#         str1.remove(i)

# print(str1)


# Question 48. Create a dictionary with number and its square from 1 to n.



# Number = int (input("Enter A Number:"))

# Dictionary = {}

# for i in range (1,Number+1):
#     Dictionary[i] =i**2

# print(Dictionary)



# Question 49. Find the average of numbers in a list.


# l1 = [10,20,2,11,40,15,14,71,12,13,50,10,10] 

# count = len(l1)

# avg=0

# for i in l1:
#     avg = i+avg;
# print("Avg Of Element in A list:",avg/count)









# Question  50. Split a string into a list of words.

# str1 = "Vikash  sir Python Ki Class loh"
# print(str1.split())


























