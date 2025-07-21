class Sample():
    def sum (self,a,b):
        return a+b
    def sum(self,a,b,c):
        return a+b+c
    def sum(self,a,b,c,d,):
        return a+b+c+d

Object = Sample()

print( "Sum Of Number IS:",Object.sum(2,3,4))

print( "Sum Of Number IS:",Object.sum(2,3,4,5))


