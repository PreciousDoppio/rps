import random

UserWins = 0
CompWins = 0

def UserFunction():
    UserChoice = input("rock paper or scissors, pick one, rn: ")
    if UserChoice in ["rock", "Rock", "r", "R", "1"]:
        UserChoice = "r"
    elif UserChoice in ["paper", "Paper", "p", "P", "2"]:
        UserChoice = "p"
    elif UserChoice in ["scissors", "Scissors", "s", "S", "3"]:
        UserChoice = "s"
    else:
        print("pick a valid option dumbass.")
        UserFunction()
    return UserChoice

def CompFunction():
    CompChoice = random.randint(1,3)
    if CompChoice == 1:
        CompChoice = "r"
    elif CompChoice == 2:
        CompChoice = "p"
    else:
        CompChoice = "s"
    return CompChoice

while True:
    print("")

    UserChoice = UserFunction()
    CompChoice = CompFunction()

    print("")

    if Userchoice == "r":
        if CompChoice == "r":
            print("you both picked rock, smh, tie.")
        elif CompChoice == "s":
            print("bro computer picked scissors, you win, that nigga dumb asf.")
            UserWins = UserWins + 1
        elif CompChoice == "p":
            print("computer picked paper, you lost bro....")
            CompWins = CompWins + 1

    elif Userchoice == "p":
        if CompChoice == "r":
            print("idk why but paper beats rock so gj i guess bro")
            UserWins = UserWins + 1
        elif CompChoice == "s":
            print("dead.")
            CompWins = CompWins + 1
        elif CompChoice == "p":
            print("tie xd")

    elif Userchoice == "s":
        if CompChoice == "r":
            print("dumb as hell, trying to cut a rock with scissors.")
            CompWins = CompWins + 1
        elif CompChoice == "s":
            print("stop tying")
        elif CompChoice == "p":
            print("computer picked paper, you win")
            UserWins = UserWins + 1

    print("")
    print("you won " + str(UserWins) + " times")
    print("comp won " + str(CompWins) + " times")
    print("")

    UserChoice = input("bro your wins aint high enough i wouldnt take it, play again? (y/n)")
    if UserChoice == "y":
        pass
    elif UserChoice == "n":
        break
