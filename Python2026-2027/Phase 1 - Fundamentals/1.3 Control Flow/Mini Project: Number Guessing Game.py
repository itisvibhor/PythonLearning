import random
print("Guess the Number between 1 - 100 ( Both Included )")
flag = 1
while flag != 0:
    secret = random.randint(1,100)
    counter = 0
    while True:
        counter = counter + 1
        guess = int(input("Enter Your Guess : "))
        if (guess == secret):
            print("Correct !")
            break
        elif(guess > secret):
            print("Too High")
        elif(guess < secret):
            print("Too Low")

        if ( counter ==10):
            print("Game Over ! Out of Attempts")
            break
        elif(counter > 4):
            if(secret - 5 <= guess <= secret + 5):
                print("You are Very Close")

    print("Thanks For Playing")
    print("Your Total Attempts : " , counter)
    check = input("Do you want to Play Again ! Yes to Continue No To Quit : ")
    if check == "No" or check == "no":
        flag =0

