# dict = {
#     "name":"Rushi",
#     "age":20,
# }
# for key,value in dict.items():
#     print(key,value)

# print(dict.get("city"))
# print(dict.get("age"))

# print(dict.get("age", "30"))
# print(dict.get("city", "sangli"))

# p = dict.clear()
# print(p)

    # dict = {
    #     x: x * x for x in range(10)
    # }
# print(dict)

# keys = ["name", "age"]
# values = ["Rushi", 20]
# dict = {
#     k : v for k, v in zip(keys, values)
# }
# print(dict)

# keys = ["name", "age"]
# values = ["Rushi", 20]
# dicti = dict(zip(keys, values))
# # print(dicti)

# sort_dict = sorted(dicti.items())
# print(sort_dict)

# keys = ["name", "age"]
# values = [50, 20]
# dicti = dict(zip(keys, values))
# sort_dict = sorted(dicti.items(), key = lambda x: x[1])
# print(sort_dict)
#
# sort_dict = sorted(dicti.items(), key = lambda x: x[1], reverse=True)
# print(sort_dict)

# dict1 = {
#     "name":"Rushi",
#     "age":20,
#     "City": "Sangli"
# }
# dict2 = {
#     "name":"Rushi2",
#     "age":202,
# }
# dict3 = dict1 | dict2
# print(dict3)

# For loops
# lst = [1,2,3,4,5]
# for i, val in enumerate(lst):
#     print(i, val)

# for i in range(3):
#     for j in range(3):
#         print(i, j)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# flat = []
# for row in matrix:
#     for i in row:
#         flat.append(i)
# print(flat[3])

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# lst = [i for sub in matrix for i in sub]
# print(lst)

# lst = [i * i for i in range(5)]
# print(lst)

# for i in "aeiour":
#     if i in "aeiou":
#         continue
#     print(i)

n = 15
# if 10 >= n <= 20:
#     print("yes")
# if 10 <= n <= 20:
#     print("in range")

# str = "sring"
# if str.isalpha() and len(str) >= 5:
    # print("String is Alphabetical")

# if 5 > 10 or 5 < 6:
#     print("yes")
# else:
#     print("no")

# user_logged = False
# if not user_logged:
#     print("Logged in")
# else:
#     print("Logged out")

# n = 49
# result = "even" if n % 2 == 0 else "odd"
# print(result)

# l1 = [1,2]
# l2 = [1,4]
# # if type(l1) == type(l2):
# if l1 == l2:
#     print("Great")

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
# print(fact(5))

# def outer():
#     def inner():
#         return "Hello"
#     return inner
# temp = outer()
# print(temp())

# def funct(a: int, b: int) -> int:
#     return a+b
# print(funct(1, 2))

# def get_even(nums):
#     return [n for n in nums if n % 2 == 0]
# print(get_even([1,2,3,4,5,6,7,8,9]))




