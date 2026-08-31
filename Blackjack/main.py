from turtledemo.round_dance import stop
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import art
import random
play=input("do you want to play the game?").lower()


def information(user, computer):
    print(f"Your cards: {user},current score {sum(user)}")
    print(f"Computer first card is: {computer[0]}")


def ace(who):
    for card in who:
        if card == 11 and sum(who) > 21:
            who.remove(11)
            who.append(1)

if play == "yes":
    print(art.logo)

    user_cards = []
    computer_cards = []

    user_card = random.sample(cards, 2)
    user_cards.extend(user_card)
    computer_card = random.sample(cards, 2)
    computer_cards.extend(computer_card)


    information(user_cards, computer_cards)
    ace(user_cards)






    k=True
    while k:
        again=input("Do you want to take another card? [yes/no]").lower()
        if again == "yes":
            user_card = random.sample(cards,1)
            user_cards.extend(user_card)
            information(user_cards, computer_cards)
            ace(user_cards)

        if sum(user_cards) ==21:
            print("You win!!!")
            break

        if again=="no"and sum(user_cards) <= 21:
            k=False
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")

            break
        if sum(user_cards) >21:
            print("You lose!!!")
            break







    while sum(computer_cards)<=17:
        computer_card = random.sample(cards,1)
        computer_cards.extend(computer_card)
        ace(computer_cards)



        if sum(computer_cards) >=17:
            break





    def compare(user,computer):
        if 21 < sum(computer):
            print(f"computer went over. YOU WİN!!!!!")
        elif sum(user) == sum(computer):
            print("Draw")

        elif sum(user) > sum(computer):
            print("You win!!!")

        elif sum(user) < sum(computer):
            print("You lose!!!")




    if sum(user_cards) <=21 and sum(computer_cards)<=21:
        print(f"computer final hand: {computer_cards}, final score: {sum(computer_cards)}")
        compare(user_cards, computer_cards)


    elif sum(user_cards)<=21 and sum(computer_cards)>21:
        print(f"computer final hand: {computer_cards}, final score: {sum(computer_cards)}")
        compare(user_cards, computer_cards)


















if play == "no":
    print("Why are yo here then????")














