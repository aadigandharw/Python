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






