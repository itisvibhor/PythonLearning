#  Q1
# number = int(input("Enter a number : "))
# print("Binary of the Number" , bin(number) , "Octal of the number" , oct(number),"Hexadecimal of the number ", hex(number),sep = " , ")

# Q2
# x = 10
# y = 15
# print("Binary x : " , bin(x), " Binary y : ", bin(y))
# print("Bitwise And : " , x & y)
# print("Bitwise Or : " , x | y)
# print("Bitwise XOR : " , x ^ y)

# Q3
# x=20
# print("Left Shift (Multiply by ) " ,x<<1)
# print("Right Shift ( Divide ) " , x>>1)

# Q4
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 !=0) or (year%400==0):
#     print("Leap Year")
# else:
#     print("Not a leap year")

# Q5
number_1 = int(input("Enter Number 1 : "))
number_2 = int(input("Enter Number 2 : "))
operator = input("Enter Operator ( + , - , * , / ) : ")
if operator == "+": 
    print("Sum of Numbers is " , number_1 + number_2)
elif operator == "-":
        print("Difference of Numbers is " , number_1 - number_2)
elif operator == "*":
          print("Product of Numbers is " , number_1 * number_2)
elif operator == "/":
    if number_2 == 0:
        print("Number 2 is 0 Kindly change it to avoid Division by Zero Error")
    else:
        print("Division of Numbers is " , number_1 / number_2)
else:
         print("Invalid Option")



