# Q1 : 
# num1 = float(int(input("Enter number 1 : ")))
# num2 = float(int(input("Enter number 2 : ")))
# print(f" Sum is {num1 + num2}")
# print(f" Difference is {num1 - num2}")
# print(f" Product is {num1 * num2}")
# print(f" Quotient is {num1 / num2}")

# Q2 : strip ()  | capitalize()
# name = input("Enter your name : ")
# name = name.strip()
# # name = name.upper()
# name = name.capitalize()
# print(f"Hello, {name}!") 

# Q3 : slice()
# s = "Python Programming"
# print(f"{s.upper()}")
# print(f"{s.lower()}")
# print(f"{s[::-1]}")

# Q4 : split()
# sentence = input("Enter a sentence : ")
# sentence = sentence.split()
# print(f"{len(sentence)}")

# Q5 : 
# print("Item 1 "," Rs 50 " , " Item 2 ", " Rs 100 " , " Item 3 "," Rs 150 ",sep = "=>", end = "=> End of Receipt")


members_list = []
counter = set()
counter.add(1)
dict_members = {"name":"Vibhor","id":counter[0]}
members_list.append(dict_members)
print(members_list[0]["name"])
print(members_list[0]["id"])
