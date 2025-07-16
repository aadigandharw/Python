# Question No.1
#       * 
#     * * * 
#   * * * * *
# * * * * * * *



# row = 5
# space = 4
# star = 1

# for i in range(row):
#     for j in range(space):
#         print(" ", end =" ")
#     for j in range (i+star):
#         print("*",end=" ")

#     print()
#     space = space-1
#     star= star+1


# Question No. 2:
# * * * * * * * 
#   * * * * * 
#     * * *
#       *

# star =7 
# space = 0
# row =4

# for i in range(row):
#     for j in range (space):
#         print(" ",end = " ")
#     for k in range (star-i):
#         print("*",end=" ")
#     print()
#     star = star-1
#     space = space+1


# Question No 3

#    * * * * * 
#    *       * 
#    *       *
#    *       *
#    * * * * *

# star = 5 
# space = 3
# row = 5

# for i in range (row):
#     if i == 0 or i == row-1:
#             for k in range(star):
#                 print("*",end = " ")

#     else:
#         for l in range (1):
#             print("*" , end = " ")
#         for m in range(space):
#             print(" ",end=" ")
#         for n in range (1):
#             print("*" , end= " ")
#     print()



# Question No. 4 
#        * 
#       * * 
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# star = 1 
# row = 5
# space = 4

# for i in range (row):

#     for j in range(space):
#         print(" ",end=" ")
#     for k in range(star):
#         print("*",end=" ")
#     print()
#     star=star+1
#     space = space-1

# star=star-1
# row = 4
# space=1
# star = star-1

# for i in range (row):
#     for j in range(space):
#         print(" ",end = " ")
#     for k in range(star):
#         print("*",end=" ")
#     print()
#     star=star-1
#     space = space+1


# Question No 5 
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# row =5 
# star=1

# for i in range(row):
#     for j in range(star):
#         print("*",end = " ")
#     print()
#     star = star +1

# star =4
# row =4
# for i in range(row):
#     for j in range(star):
#         print("*" ,end = " ")
#     star = star -1
#     print()



# Question No 6 
# * * * * * 
# *   *   *
# *   *   *
# *   *   *
# * * * * *

# row = 5 
# star = 5 


# for i in range (row):
#     if i == 0 or i == row-1:
#         for j in range(star):
#             print("*",end=" ")
#         print()
#     else:
#         for k in range(1):
#             print("*" , " " ,"*" , " " , "*")



# Question No :7
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# row = 5
# col = 5 

# for i in range(row):
#     for j in range(col):
#         print(i+1 ,end=" ")
#     print()

# Question No. 8 


# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# row = 5
# col = 1

# for i in range(row):
#     for j in range(col):
#         print(i+1,end=" ")
#     print()
#     col = col+1



# Question No.9

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# row = 5
# col = 1
# for i in range(row):
#     for j in range(col):
#         print(j+1,end=" ")
#     print()
#     col = col+1


# Question No.10

#         1 
#       2 1 2
#     3 2 1 2 3 
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

# row = 1
# num= 1

# MainRow = int(input("Enter A Number :"))

# space = MainRow

# for i in range (MainRow):
#     for i in range (space):
#         print(" ",end = " ")

#     for j in range (row):
#         print(num,end = " ")
#         num = num-1

#     num = row

#     for k in range(1,num):
#         print (k+1,end=" ")
#         k = k + 1
    
#     print()
#     row = row + 1
#     num = row
#     space = space - 1




# Question 11

#         * 
#       *   * 
#     *       * 
#   *           * 
# *               * 
#   *           * 
#     *       * 
#       *   * 
#         * 

# Total_row = 5

# space = 4
# space2 = 1

# row =1 
# round1 = 1

# for i in range (5):
#     if i == 0 :
#         for j in range (space):
#             print(" " , end = " ")
#         print("*" ,end = " ")
#     else :
#         for k in range (space):
#             print(" " , end = " ")
#         print("*",end = " ")
#         for l in range(2,space2):
#             print(" ",end = " ")
#         print("*" , end = " ")

#     print()
#     space = space -1 
#     space2 = space2+2

# # print (space,space2)

# space =  1 
# space2 = 7

# for i in range (4):
#     if i == 3:
#         for j in range (space):
#             print(" " , end = " ")
#         print("*" ,end = " ")
#     else :
#         for k in range (space):
#             print(" " , end = " ")
#         print("*",end = " ")
#         for l in range(2,space2):
#             print(" ",end = " ")
#         print("*" , end = " ")
#     print()
#     space2 = space2 - 2
#     space = space + 1



# Question 12 :
# 1 
# 2 3 
# 3 4 5 
# 4 5 6 7 
# 5 6 7 8 9 
# 6 7 8 9 10 11 
# 7 8 9 10 11 12 13 
# 8 9 10 11 12 13 14 15 
# 9 10 11 12 13 14 15 16 17 
# 10 11 12 13 14 15 16 17 18 19 


# Main_row = int (input("Enter A How Many Rows You Want To Print:"))
# row = 1 
# num = 1 
# while row <= Main_row:
#     for i in range (row):
#         print(num , end = " ")
#         num = num+1
#     print()
#     num = row + 1
#     row = row + 1



# Question : 

#       *  
#     * * *  
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *  
#       *




# star = 1 
# row = 7 
# space = 4 

# for i in range (row):
#     for j in range (space):
#         print(" ", end=" ")
#     for k in range (star):
#         print("*" , end = " ")
#     if i >= 3 :
#         star = star - 2
#         space = space + 1
#     else:
#         star = star + 2 
#         space = space - 1
#     print()


# Question :

# * * * * *  
# *
# *
# * * * * *  
# * 
# * 
# * * * * *

# row = 7 
# star = 4 

# for i in range (row):
#     if i == 0 or i == 3 or i == 6 :
#         for i in range(star):
#             print("*" , end = " ")
            
    
#     print("*")
    


# 0 
#   1 
#     3 
#       8 
#     5
#   2 
# 1

# num = 0 
# space = 0 
# row = 7
# add = 0

# for i in range (row):
#     for i in range(space):
#         print(" ", end = " ")
#     print(num ,end =" ")
#     print ()
#     num = num + 1
#     space = space + 1




def fib(n): 
    fib=[0,1] 
    for a in range(2,n): 
        fib.append(fib[a-2]+fib[a-
1]) 
    return fib 
a=fib(7) 
f=a[::2] 
s=a[1::2] 
t=s[::-1] 
z=f+t 
n=7 
space=0 
for a in range(n): 
    print('  '*space,end='') 
    print(z[a]) 
    space=space+1 if a<n//2 
else:
    space-1