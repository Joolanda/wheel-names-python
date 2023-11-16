import random

def pick_name_wheel():
    print("Check out my Name Picker")
    listname = input("Enter names separated by commas: ")
    names = listname.split(",")

    while len(names) > 0:
        print("Spinning the wheel...\n")
        winner = random.choice(names)
        print("The winner is:", winner)
        names.remove(winner)

        play_again = input("Spin again? yes/no: ")
        if play_again.lower() != "yes":
            print("Bye! See you next time.")
            break

if __name__ == "__main__":
    pick_name_wheel()

