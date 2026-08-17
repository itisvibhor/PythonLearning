# Q1
# def describe_person(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# describe_person(name="Goli",age=25,city="delhi",gender="male")

# Q2
# def factorial(n):
#    if n == 0:
#       return 1
#    return n * factorial(n-1)

# result = factorial(5)
# print(result)

# Q3
# def safe_divide(a,b):
#     if b ==0:
#         return "Enter b again as it cannot be 0"
#     else:
#         return a/b
# print(safe_divide(10,20))

# Q4
# def bug_checker(a,my_list=[]):
    # if my_list == None:  // dont consider
    #     my_list = []// dont consider
#         my_list.append(a)
#         for i in my_list:
#             print(i)
# bug_checker(1)
# bug_checker(2)

# Q5
# people = [("Rahul", 25), ("Priya", 22), ("Aman", 30)]
# sorted_people = sorted(people,key = lambda x : x[1])
# print(sorted_people)

