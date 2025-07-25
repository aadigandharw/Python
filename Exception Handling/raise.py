try:
    n = int(input("Enter The Number: "))

    if n%2!= 0:
        raise Exception("Not A Even")
except Exception as msg:
    print(msg)
else:
    print("Even")