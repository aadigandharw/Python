# Example No 1 

try:
    x = 10
    print("Inside The Block")
    print(x)

except:
    print("Inside The Except Block")


# Example No 2

try: 
    num = 120 
    l=[2,5,6,'a',0] 
    for i in l: 
        print(num//i) 
except ZeroDivisionError: 
    print('ZeroDivision error occured') 
except IndexError: 
    print('index error occured') 
except: 
    print('unknown error occured')