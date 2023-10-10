# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = map(lambda x: x**2, numbers)
# result_list = list(result)
# print(result_list)

# import functools
# numbers = [1, 2, 3, 4, 5]
# result = functools.reduce(lambda m, n: m*n, numbers)
# print(result)
# the result is 35

# my_list = ['I', 'want', 'to', 'become', 'a', 'Software', 'Engineer']
# sorted_list = sorted(my_list, key = lambda x: len(x))
# print(sorted_list)

# my_list = ['I', 'want', 'to', 'become', 'a', 'Software', 'Engineer']
# sorted_list = sorted(my_list, key = lambda x: len(x), reverse=True)
# print(sorted_list)

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
# students = [
#     student('Titus', 20),
#     student('Brandon', 48),
#     student('Esther', 36),
#     student('Tricia', 42)
# ]        
# filtered_students = filter(lambda student: student.marks >40, students)
# filtered_students_list = list(filtered_students)
# for student in filtered_students_list:
#     print(f"{student.name} has marks greater than 40." )

# def outer_function(a):
#     def inner_function(b):
#         return a*b
#     return inner_function
# closure1=outer_function(2)
# closure2=outer_function(4)
# result1=closure1(5)
# result2=closure2(5)
# print(result2)

# user_database = {
#     'user1' : 'password1',
#     'user2' : 'password2',
# }
# def authenticate(username, password):
#     def decorator_function(original_function):
#         def wrapper_function(*args, **kwargs):
#             if username in user_database and user_database[username] == password:
#                 print(f"authentification successful for {username}.")
#                 return original_function(*args, **kwargs)
#             else:
#                 print(f"authentification failed for {username}.")
#                 return None
#             return wrapper_function
#         return decorator_function
#     @authenticate(username='user1', password='password1')
#     def protected_function():
#         print("this is a protected function.")
        
# import time

# def timing_decorator(original_function):
#     def wrapper_function(*args, **kwargs):
#         start_time = time.time()
#         result = original_function(*args, **kwargs)
#         end_time = time.time()
#         print(f"{original_function.__name__} ran in {end_time - start_time} seconds")
#         return result
#     return wrapper_function

# @timing_decorator
# def some_function():
#     # Simulate a time-consuming task
#     time.sleep(2)

# some_function()

# #OBJECT ORIENTED PROGRAMMING
# class Human:
#         attr1 = "female"
#         attr2 = "18"
#         def fun(self):
#             print("i am a", self.attr1)
#             print("i am", self.attr2)
# Tricia=Human()     
# print(Tricia.attr1)
# Tricia.fun()   

#SELF PARAMETER
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#     def show(self):
#             print("my dog's name is "+self.name+" and it's a "+self.breed+".")
# obj=Dog("Lucky", "chiwawa")
# obj.show()

# Base class (parent class)
# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def area(self):
#         pass

# # Another derived class (child class) inheriting from Shape
# class Rectangle(Shape):
#     def __init__(self, color, length, width):
#         super().__init__(color)
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# # Create instances of the derived classes
# blue_rectangle = Rectangle("Blue", 4, 6)

# # Calculate and print the areas of the shapes
# print(f"Area of the blue rectangle: {blue_rectangle.area()}")

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

# OOP
# class human:
#     attr1="girl"
#     attr2="walk"
#     def fun(self):
#         print("I am a", self.attr1)
#         print("I can", self.attr2)
# Tricia=human()
# Tricia.fun()        

# class human:
#     def __init__(self, name, gender):
#         self.name = name 
#         self.gender = gender
#     def show(self):
#         print("my name is "+self.name+" and am a girl")
# obj = human("Tricia", "girl")
# obj.show()      

#SUPER EXAMPLE  

# class Task:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#         self.completed = False
   