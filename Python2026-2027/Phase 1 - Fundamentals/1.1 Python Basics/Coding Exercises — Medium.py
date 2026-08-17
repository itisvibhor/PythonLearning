# Q1
# name = input("Enter Messy Text : ")
# name = name.split()
# print(f"{' '.join(name).title()}")

# Q2
# temp = float(input("Enter Temp : "))
# temp_f = ((temp * 2) -  ((temp * 2) * 10 / 100 ) ) + 32
# print(f" {temp} C => {temp_f:.2f} F")

# Q3 Question was not possible with the help of 1.1 Basics only so loops are used
# numbers = input("Enter numbers seperated by commas : ")
# total = 0 
# count = 0 
# numbers = numbers.split(",")
# for i in numbers:
#     i=i.strip()
#     total = total + int(i)
#     count = count + 1
# print(f"Total Sum is : {total} and the Average is : {total/count}")

# Q4
# price = float(input("Enter the price : "))
# discount = float(input("Enter the discount in % : "))
# # print(f"Final Price : ${price - ((price * discount)/100):.2f}")
# final_price = price - ((price * discount)/100)
# print(f"Final Price is ${final_price:.2f}")

# Q5
# print("I am a Type Detective")
# value = input("Input your Text / Number / Float Value : ")
# if value.isdigit():
#     print("Integer")
# elif value.count(".")==1:
#     parts = value.split(".")
#     if parts[0].isdigit() & parts[1].isdigit():
#         print("Its a Float")
#     else:
#         print("Looks like a plain Text")
# else:
#     print("Plain Text")       
