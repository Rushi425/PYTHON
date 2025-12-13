# def greeting(name):
#     print("Hello,",name)
# greeting("RRR")

# def square(n):
#     return n*n
# print(square(5))

# def greet(n, name = "Rushi"):
#     print("Hello, " ,name)
# greet("FFF", 5)

# def calc(a, b):
#     return a + b, a * b
# # print(calc(1, 2))
# temp = calc(4,4)
# print(temp)


# def funct(dict):
#     for k in dict:
#         print(k)
#
# dict = {
#     "name": "Rushi",
#     "age": 15
# }
# print(funct(dict))
# funct(dict)

# def funcWithArgs(*nums):
#     # print(sum(nums))
#     print(len(nums))
# funcWithArgs(1, 2, 3)

# def show_details(**info):
#     print(info)
# show_details(**{"a":1, "b":2, "c":3})

# def info(**details):
#     print("Name:", details["name"])
#     print("Age:", details["age"])
#     try:
#         print("Age:", details["agte"])
#     except:
#         print("not exist")
#
# info(name="Rushi", age=20)

# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# demo(1, 2, 3, name="Rushi", age=20)

# sqaure = lambda n: n * n
# print(sqaure(10))

# def funct(n):
    # return lambda x: x * n
# f = funct(3)
# print(f(3))

# nums = [1,2,3,4]
# res = map(lambda x: x + x, nums)
# print(list(res))

# nums = [1,2,3,4]
# res = filter(lambda x: x > 2, nums)
# print(list(res))

# nums = [1,2,3,4,5,6]
# even = filter(lambda x: x % 2 == 0, nums)
# print(list(even))