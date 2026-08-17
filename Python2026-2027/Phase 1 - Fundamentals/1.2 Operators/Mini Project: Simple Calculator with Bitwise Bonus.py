print("Mini Project : Simple Calculator")
my_list=[]
flag=0
while flag == 0:
    number_1 = input("Enter First Number : ")
    number_2 = input("Enter Second Number : ")
    if(number_1.isdigit() and number_2.isdigit()):
        number_1 = int(number_1)
        number_2 = int(number_2)
        print("Select Calculation Menu Choice")
        print("1. Simple Calculator Menu")
        print("2. Bitwise Operators Menu")
        menu_choice = int(input("Enter your option : "))
        if(menu_choice == 1):
            print("Calculator Menu. Select An Option From The Following:")
            print("1. +")
            print("2. -")
            print("3. *")
            print("4. /")
            print("5. //")
            print("6. %")
            print("7. **")
            choice = int(input("Enter Your Choice Of Operator : "))
            print("Operator Chosen is No. " , choice)
            if (choice == 1):
                add = number_2 + number_1
                print(number_1 + number_2)
                my_list.append(add)
            elif(choice == 2):
                print(number_1 - number_2)
            elif(choice == 3):
                print(number_1 * number_2)
            elif(choice == 4):
                if( number_2 ==0):
                    print("Divide by zero error! Kindly Try Again")
                else:
                    print(round(number_1 / number_2),2)
            elif(choice == 5):
                print(number_1 // number_2)
            elif(choice == 6):
                print(number_1 % number_2)
            elif(choice == 7):
                print(number_1 ** number_2)
            else:
                print("Invalid Option! You Want to try again? Type 'Exit' to Quit")
        elif(menu_choice ==2):
            print("1. AND")
            print("2. OR")
            print("3. XOR")
            bitwise_operator_choice = int(input("Select a Bitwise Operator : "))
            if(bitwise_operator_choice == 1):
                print(number_1 & number_2)
            elif(bitwise_operator_choice == 2):
                print(number_1 | number_2)
            elif(bitwise_operator_choice == 3):
                print(number_1 ^ number_2)
            else:
                print("Invalid Option. Try Again !")
        else:
            print("Invalid Option. Try Again !")
    print("Last  5 Results")
    for i in my_list[-5:]:
        print(i)
    