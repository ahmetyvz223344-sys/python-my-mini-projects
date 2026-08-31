logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import game_data
import random

def random_person():
    number=random.randint(0,49)
    return number
A=[]
B=[]

feature=["name","follower_count","description","country"]
def features(x):
    x.clear()
    a=game_data.data[random_person()]

    name=a["name"]
    x.append(name)
    follower_count=a["follower_count"]
    x.append(follower_count)
    description=a["description"]
    x.append(description)
    country=a["country"]
    x.append(country)




def game():
    features(A)
    features(B)
    print(logo)
    print(f"Compare A:{A[0]}, {A[2]}, from {A[3]}")
    print(vs)
    print(f"Against B:{B[0]}, {B[2]}, from {B[3]}")


game()

guess = input("Who has more followers? Type A or B").upper()

def compare(a,b):


    if a[1]>b[1] and guess=="A":

        return True


    elif a[1]<b[1] and guess=="B":


        return True


    else:
        return False


compare(A,B)



def new_game():
    features(B)
    print(logo)
    print(f"Compare A:{A[0]}, {A[2]}, from {A[3]}")
    print(vs)
    print(f"Against B:{B[0]}, {B[2]}, from {B[3]}")





c = []


while True:
    if compare(A,B)==True:
        if B[1] > A[1]:
            A = B.copy()



        print("\n"*20)
        new_game()
        c.append(1)
        print(f"You're right! Current score:{len(c)}")

        guess=input("Who has more followers? Type A or B")






    elif compare(A,B)==False:
        print(logo)
        print(f"Sorry, {guess} is wrong. Final score:{len(c)}")
        break




#hocanın çözümü



from art import logo
from game_data import data
import random


def check_answer(user_guess,a_followers,b_followers):
    '''take the user guess and the follower counts and returns if they got it right?'''
    if a_followers>b_followers:
        return user_guess=="A"
    else:
        return user_guess=="B"












print(logo)

score=0
game_should_continue=True
account_b=random.choice(data)

while game_should_continue:

    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    def format_data(account):

        account_name=account["name"]
        account_descr=account["description"]
        account_country=account["country"]

        return(f"{account_name} a {account_descr} from {account_country}")



    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")

    guess=input("Who has more followers? Type A or B")
    print("\n"*20)
    print(logo)


    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    is_correct=check_answer(guess,a_follower_count,b_follower_count)


    if is_correct:
        score+=1
        print(f"You're right! Current score:{score}")

    else:
        print(f"Sorry, {guess} is wrong. Final score:{score}")
        game_should_continue=False
