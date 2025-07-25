try:
    ad = 0 
    l = [1,2,3,'a']
    for i in l:
        ad += i
    
except:
    print("Error Occurred")

else:
    print("No Error Are There")

finally:
    print(ad)