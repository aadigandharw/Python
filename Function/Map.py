l = [2,3,4,5,6]

n = list(map(lambda n : n**2,l ))
print (n)



def square (n):
    return n ** 2 
l = [1,2,3,4,5,6,7,8,9]

n = list(map(square,l))
print(n)


def multiply (n):
    return 5*n
l = [1,2,3,4,5,6,7,8,9,10]
n = list(map(multiply,l))
print(n)