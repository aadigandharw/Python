try:
    n = 5
    assert n % 2 == 0 , "It's not Even "
except AssertionError as msg:
    print(msg)

else:
    print("Even")