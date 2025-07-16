l = [1,2,3,4,5,6,7,8,9,0,11,12,23,25]

n = list(filter(lambda n : n%2 !=0 ,l))

print(n)



def Even (n):
    return n%2==0

n = list(filter(Even,l))
print(n)