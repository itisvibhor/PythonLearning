generate_card = True
while generate_card:
        input_name = input("Enter your name : ")
        input_age = int(input("Enter your age : "))
        input_height = float(input("Enter your height(cm) : "))
        input_weight =float(input("Enter your weight(kg) : "))
        input_name = input_name.split()
        input_name = " ".join(input_name).strip().title()
        calculated_bmi = input_weight / (( input_height/100) ** 2)
        print("=" * 24)
        print("      PROIFLE CARD")
        print("=" * 24)
        print("Name",input_name,sep = " : ")
        print("Age",input_age,sep = " : ")
        print("Height",input_height ,sep = " : ")
        print("Weight",input_weight ,sep = " : ")
        print("BMI",round(calculated_bmi,2) ,sep = " : ")
        print("=" * 24)
        if calculated_bmi >= 30:
            print("You are Obese")
        elif calculated_bmi < 30 and  calculated_bmi >= 25:
            print("You are Over Weight")
        elif calculated_bmi < 25 and calculated_bmi >=18:
            print("You are Normal")
        else:
            print("You are Under Weight")
        input_option = input("Generate Another Profile Card (Type Quit To Exit) : ")
        if input_option == "Quit" or input_option == "quit":
            generate_card = False
        