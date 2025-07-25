# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))


def count_to_up(n):
    num = 1
    while num <= n:
        yield num 
        num += 1
    
for i in count_to_up(5):
    print(i)









