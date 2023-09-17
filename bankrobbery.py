import time
import sys

def printtw(string):
    for char in string:
        time.sleep(0.1)
        print(char, end="")
        sys.stdout.flush()
    print()

print("Welcome to the Bank Robbery Adventure!")
printtw("You find yourself in front of a bank, ready to execute a daring heist.")
printtw("You have two options at each step. Choose wisely!")

# First Decision
printtw("\nYou enter the bank and approach the front desk.")
printtw("1) Quietly demand the money from the bank teller")
printtw("2) Fire your gun into the air to create chaos")

decision_1 = input("Choose 1 or 2: ")

if decision_1 == "1":
    printtw("The bank teller nervously hands over the money. You've taken the first step.")
    # Second Decision
    printtw("\nWith the money in hand, you head towards the exit.")
    printtw("1) Make a discreet exit through the back door")
    printtw("2) Burst through the front doors, guns blazing")

    decision_2 = input("Choose 1 or 2: ")

    if decision_2 == "1":
        printtw("You quietly exit through the back door, avoiding attention.")
        # Third Decision
        printtw("\nYou're now outside, but the police are closing in.")
        printtw("1) Try to steal a nearby car to escape")
        printtw("2) Hide in an alleyway and hope the police pass by")

        decision_3 = input("Choose 1 or 2: ")

        if decision_3 == "1":
            printtw("You successfully hotwire a car and make a quick getaway.")
            printtw("Congratulations, you've escaped with the stolen money!")

            printtw("\nYou've managed to pull off the bank robbery and escape successfully!")
            printtw("You're now a notorious criminal, living life on the run.")
        else:
            printtw("You hide in the alleyway, but the police eventually find you.")
            printtw("Your character has met a tragic end. Game Over!")
    else:
        printtw("You burst through the front doors, triggering an intense gunfight with the police.")
        printtw("Your character has met a tragic end. Game Over!")


else:
    printtw("Your gunshot causes panic! The police are alerted, and you're surrounded.")
    printtw("Your character has met a tragic end. Game Over!")

