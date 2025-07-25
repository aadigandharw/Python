try:
    l = [10,20,30]
    x = 60
    for i in l:
        print(x//i)
except(ZeroDivisionError,TypeError) as msg:
    print(msg)
except:
    print("Unexpected Error")

else:
    print("No Error!!!")