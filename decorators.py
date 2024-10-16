# def my_dec(func):
#     def wrapper():
#         print("something is happening before the function is called.")
#         print(func() ** 2)
#         print("something is happening before the function is called.")
#     return wrapper

# @my_dec
# def say_hello():
#     return 7
# say_hello() 



# decorator with an ARGUMENT
# def my_dec(func):
#     def wrapper(*args): 
#         print("something is happening before the function is called.")
#         print(func(*args))
#         print("square of the num")
#     return wrapper

# @my_dec
# def say_hi(num, num2):
#     return num + num2
# say_hi(5, 5)  



# несколько декораторов
# def dec1(func):
#     def wrapper():
#         print("dec1")
#         func() 
#     return wrapper

# def dec2(func):
#     def wrapper():
#         print("dec2")
#         func()
#     return wrapper

# @dec1
# @dec2
# def say_hi():
#     print("hello")
# say_hi()  



# декор с аршументом у себя
# def repeat(num):
#     def dec_repeat(func):
#         def wrapper(*args):
#             for _ in range(num):
#                 func(*args)
#         return wrapper
#     return dec_repeat

# @repeat(5)
# def say_hi(name):
#     print(f"hello {name}")

# say_hi("ali")  






# def dec_check(func):
#     def wrapper():
#         if func() > 10:
#             print("grater than 10")
#         else:
#             print("less than 10")
#     return wrapper

# @dec_check
# def check():
#     result = int(input("enter num: "))
#     print(result)
#     return result 
# check() 


# def dec(func):
#     def wrapper():
#         return func()
#     return wrapper
# @dec
# def hi():
#     try:
#         num = 1
#         word = "1"
#         res = num + word
#         print(res)  
#     except Exception:
#         print("an exception occured")
#     else:
#         print("alles gut!") 
# hi()  


# def main(func):
#     def wrapper():
#         func()
#     return wrapper
# @main
# def hi():
#     user_input = int(input("enter any num: "))
#     num = user_input % 2 
#     if num == 0:
#         print("result is not an odd number!")
#     else:
#         print("result is an odd num!") 
# hi() 