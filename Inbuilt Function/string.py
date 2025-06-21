# Set Inbuilt function

# 1 Upper()

# a = "Jitendra"
# print(a.upper())

# name = "aditya"
# print(name.upper())

# sentence = "python is awesome"
# print(sentence.upper()) 

# user_input = input("Enter something: ")  # e.g., "good morning"
# print(user_input.upper()) 


# 2 Lower ()

# a = "Jitendra"
# print(a.lower())

# name = "aditya"
# print(name.lower())

# sentence = "python is awesome"
# print(sentence.lower()) 

# user_input = input("Enter something: ")  # e.g., "good morning"
# print(user_input.lower()) 


# 3 Capitalized 

# a = "Jitendra"
# print(a.capitalize())

# name = "aditya"
# print(name.capitalize())

# sentence = "python is awesome"
# print(sentence.capitalize()) 

# user_input = input("Enter something: ")  # e.g., "good morning"
# print(user_input.capitalize()) 

# 4 tittle 

# a = "Jitendra"
# print(a.title())

# name = "aditya"
# print(name.title())

# sentence = "python is awesome"
# print(sentence.title()) 

# user_input = input("Enter something: ")  # e.g., "good morning"
# print(user_input.title()) 

# 5 Index()

# text = "hello"
# print(text.index("e"))

# sentence = "python is awesome"
# print(sentence.index("is"))

# msg = "banana"
# print(msg.index("a", 2))  # Output: 3 start From Specific Position


# 6 # rindex ()

# text = "hello"
# print(text.rindex("e"))

# sentence = "python is awesome"
# print(sentence.rindex("is"))

# msg = "banana"
# print(msg.rindex("a", 2))

# 7 find()

# text = "hello"
# print(text.find("e"))

# sentence = "python is awesome"
# print(sentence.find("is"))

# msg = "banana"
# print(msg.find("a", 2))

# 8 rfind()

# text = "hello"
# print(text.rfind("e"))

# sentence = "python is awesome"
# print(sentence.rfind("is"))

# msg = "banana"
# print(msg.rfind("a", 2))

# 9 split()

# sentence = "Python is awesome"
# print(sentence.split())  

# data = "apple,banana,grape"
# print(data.split(","))  

# date = "2025-06-18"
# print(date.split("-"))  

# # 10 Replace

# text = "I love Java"
# print(text.replace("Java", "Python"))  

# word = "banana"
# print(word.replace("a", "o")) 

# line = "Hello hello HeLLo"
# print(line.replace("Hello", "Hi"))  
# # Output: Hi hello HeLLo

# text = "spam spam spam"
# print(text.replace("spam", "eggs", 2))  
# # Output: eggs eggs spam


# 11 Count()

# word = "banana"
# print(word.count("a"))  

# text = "python is fun and python is powerful"
# print(text.count("python"))  

# msg = "Hello hello HELLO"
# print(msg.count("hello"))  
# # Output: 1

# text = "abababab"
# print(text.count("ab", 2, 6))  
# # Output: 2


# List InBuilt function 

# Add Methods

# 1 Append()

# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers) 

# fruits = ["apple", "banana"]
# fruits.append("orange")
# print(fruits) 

# data = [10, 20]
# data.append([30, 40])
# print(data)  

# names = []
# name = input("Enter a name: ")  # e.g., "Aditya"
# names.append(name)
# print(names)  
# # Output: ['Aditya']


# 2 Insert()

# fruits = ["banana", "orange"]
# fruits.insert(0, "apple")
# print(fruits)  
# # Output: ['apple', 'banana', 'orange']

# numbers = [1, 2, 4, 5]
# numbers.insert(2, 3)
# print(numbers)  
# # Output: [1, 2, 3, 4, 5]

# colors = ["red", "green"]
# colors.insert(len(colors), "blue")
# print(colors)  
# # Output: ['red', 'green', 'blue']

# items = [10, 20, 30]
# items.insert(1, [100, 200])
# print(items)  
# # Output: [10, [100, 200], 20, 30]

# 3 Extend ()

# fruits = ["apple", "banana"]
# fruits.extend(["mango", "orange"])
# print(fruits)

# nums = [1, 2]
# nums.extend((3, 4))
# print(nums)

# letters = ["a", "b"]
# letters.extend("cd")
# print(letters)
# # Output: ['a', 'b', 'c', 'd']


# Element  Remove inbuilt Function in List

# 1 Remove()

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)
# # Output: ['apple', 'cherry']

# numbers = [1, 2, 3, 2, 4]
# numbers.remove(2)
# print(numbers)
# # Output: [1, 3, 2, 4]


# colors = ["red", "green"]
# colors.remove("blue")
#  # Output: Value Error


# 2 Pop ()

# fruits = ["apple", "banana", "cherry"]
# last_item = fruits.pop()
# print(last_item)     # Output: cherry
# print(fruits)        # Output: ['apple', 'banana']

# numbers = [10, 20, 30, 40]
# removed = numbers.pop(1)
# print(removed)       # Output: 20
# print(numbers)       # Output: [10, 30, 40]


# numbers = [10, 20, 30, 40]
# numbers.pop(50);
# # Output:IndexError: pop index out of range

# 3 Clear ()

# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print(fruits)
# # Output: []

# 4 Sort()

# numbers = [5, 2, 9, 1]
# numbers.sort()
# print(numbers)
# # Output: [1, 2, 5, 9]

# marks = [88, 95, 70, 100]
# marks.sort(reverse=True)
# print(marks)
# # Output: [100, 95, 88, 70]


# # 5 Join()

# words = ["Python", "is", "awesome"]
# sentence = " ".join(words)
# print(sentence)
# # Output: Python is awesome

# fruits = ["apple", "banana", "cherry"]
# result = ", ".join(fruits)
# print(result)
# # Output: apple, banana, cherry

# 6 Slice ()

# fruits = ["apple", "banana", "cherry", "mango", "orange"]
# print(fruits[1:4])
# # Output: ['banana', 'cherry', 'mango']

# text = "Python Programming"
# print(text[0:6])
# # Output: Python

# nums = [1, 2, 3, 4, 5, 6]
# print(nums[::2])
# # Output: [1, 3, 5]


# 3 Set Inbuilt Method ()

# 1 To Add element In Set 

# Add()

# myset = {1, 2, 3}
# myset.add(4)
# print(myset)
# # Output: {1, 2, 3, 4}

# myset = {1, 2, 3}
# myset.add(2) 
# print(myset)
# # Output: {1, 2, 3}

# colors = {"red", "green"}
# colors.add("blue")
# print(colors)
# # Output: {'green', 'red', 'blue'}

# Update ()

# a = {1, 2}
# b = {3, 4}
# a.update(b)
# print(a)
# # Output: {1, 2, 3, 4}

# fruits = {"apple", "banana"}
# new_fruits = ["mango", "cherry"]
# fruits.update(new_fruits)
# print(fruits)
# # Output: {'banana', 'apple', 'cherry', 'mango'}

# colors = {"red"}
# colors.update(("green", "blue"))
# print(colors)
# # Output: {'blue', 'green', 'red'}

# s = {"A"}
# s.update("BCD")
# print(s)
# # Output: {'D', 'C', 'B', 'A'}

# Remove Element in Set 

# 1 Remove()

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
# # Output: {'apple', 'cherry'}


# colors = {"red", "blue"}
# colors.remove("green")
# # ❌ KeyError: 'green'

# 2 Discard()

# colors = {"red", "blue"}
# colors.discard("green")  # No error even if not present
# print(colors)
# # Output: {'red', 'blue'}

# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)
# # Output: {'apple', 'cherry'}

# 3 pop ()

# fruits = {"apple", "banana", "cherry"}
# item = fruits.pop()
# print("Popped:", item)
# print("Remaining:", fruits)
# # Output might be:
# # Popped: banana
# # Remaining: {'apple', 'cherry'}

# nums = {1, 2, 3}
# while nums:
#     print("Removed:", nums.pop())
# # Output:
# # Removed: 1
# # Removed: 2
# # Removed: 3

# 4 clear()

# colors = {"red", "blue", "green"}
# colors.clear()
# print(colors)
# # Output: set()

# 4 Dictionary Inbuilt Method


# 1 get()

# student = {"name": "Ravi", "age": 20}
# print(student.get("name"))    # Ravi
# print(student.get("gender"))  # None

# 2. .keys() / .values() / .items()

# info = {"id": 101, "name": "Neha"}

# print(info.keys())    # dict_keys(['id', 'name'])
# print(info.values())  # dict_values([101, 'Neha'])
# print(info.items())   # dict_items([('id', 101), ('name', 'Neha')])


# 3. .update()

# a = {"x": 1}
# b = {"y": 2}
# a.update(b)
# print(a)  # {'x': 1, 'y': 2}

# 4. .pop()

# d = {"a": 10, "b": 20}
# d.pop("a")   # Removes 'a'
# print(d)     # {'b': 20}

# 5 Remove()

# d = {"x": 100, "y": 200}
# d.popitem()  # Removes last added pair
# print(d)     # {'x': 100}

# 6. .clear()

# d = {"a": 1, "b": 2}
# d.clear()
# print(d)  # {}

# 8. .setdefault()

# person = {"name": "Ravi"}
# person.setdefault("age", 25)
# print(person)  # {'name': 'Ravi', 'age': 25}