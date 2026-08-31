import random
logo='''.__   __.  __    __  .___  ___. .______    _______ .______           _______  __    __   _______  _______     _______. __  .__   __.   _______      _______      ___      .___  ___.  _______ 
|  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \         /  _____||  |  |  | |   ____||   ____|   /       ||  | |  \ |  |  /  _____|    /  _____|    /   \     |   \/   | |   ____|
|   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |       |  |  __  |  |  |  | |  |__   |  |__     |   (----`|  | |   \|  | |  |  __     |  |  __     /  ^  \    |  \  /  | |  |__   
|  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /        |  | |_ | |  |  |  | |   __|  |   __|     \   \    |  | |  . `  | |  | |_ |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.   |  |__| | |  `--'  | |  |____ |  |____.----)   |   |  | |  |\   | |  |__| |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
|__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|    \______|  \______/  |_______||_______|_______/    |__| |__| \__|  \______|     \______| /__/     \__\ |__|  |__| |_______|
                                                                                                                                                                                              '''
print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

difficulty=input("Choose a difficulty level: easy or hard").lower()

if difficulty=="easy":
    number=random.randint(1,101)
    attempt = 10
    print("You have 10 attempts remaining the guess the number")


    def user_guess():
        guess = int(input("Guess a number between 1 and 100"))
        return guess



    while  attempt>0:
        guessed_number=user_guess()


        if guessed_number == number:
            print(f"You got it,the answer was {number}")
            break

        elif guessed_number > number:
            print("Too high")
            print("guess again")
            attempt = attempt - 1

            print(f"you have {attempt} remaining the guess the number")
            if attempt==0:
                print("You lose")
                break

        elif guessed_number < number:
            print("Too low")
            print("guess again")
            attempt = attempt - 1
            print(f"you have {attempt} remaining the guess the number")
            if attempt==0:
                print("You lose")
                break





elif difficulty=="hard":
    number = random.randint(1, 101)
    attempt = 5
    print("You have 5 attempts remaining the guess the number")


    def user_guess():
        guess = int(input("Guess a number between 1 and 100"))
        return guess


    while attempt > 0:
        guessed_number = user_guess()

        if guessed_number == number:
            print(f"You got it,the answer was {number}")


            break

        elif guessed_number > number:
            print("Too high")
            print("guess again")
            attempt = attempt - 1

            print(f"you have {attempt} remaining the guess the number")
            if attempt == 0:
                print("You lose")
                break

        elif guessed_number < number:
            print("Too low")
            print("guess again")
            attempt = attempt - 1
            print(f"you have {attempt} remaining the guess the number")
            if attempt == 0:
                print("You lose")
                break
