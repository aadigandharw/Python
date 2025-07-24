def decorator_function(original_function):
    def wrapper_function():
        print("Extra functionality before the original function")
        original_function()
        print("Extra functionality after the original function")
    return wrapper_function


@decorator_function
def say():
    print("Hello,Aaduuu!!")

say()