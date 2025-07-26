# WAP to print how many Characters are found in a file 
# fo = open('data.txt','r')

# x = fo.read()
# print(len(x))


# 2) wap to print how many words are found in a file 
# fo=open("data.txt",'r') 
# x=fo.read() 
# n=x.split() 
# print(len(n))


# 3) wap to print how many lines are present in a file. 


# fo=open("data.txt", "r") 
# fo.readlines() 
# fo.seek(1) 
# l=fo.readlines() 
# print(len(l))


# 4 WAP to print all The words which are starting with 'ha' 

fo = open('data.txt','r')
x = fo.read()
y = x.split()
for i in y:
    if i.startswith('ha'):
        print(i)
