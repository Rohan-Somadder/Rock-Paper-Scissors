import random
from getch import pause
import os
import csv

choices = ["rock","paper","scissors"]


class User:
    def __init__(self):
        self.name=input("\nEnter your name : ")
        self.points = 0

    def update_points(self,r):
        if r == 2:
            self.points+=3
        elif r == 1:
            self.points+=1
        elif r ==0:
            self.points-=1
    
    def return_data(self):
        return [self.name,self.points]
    
    def __str__(self):
        return "\nYour score is: "+ str(self.points)


def Game_rules():
    print('\nA player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors"),\
         \nbut will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper").\
         \nIf both players choose the same shape, the game is tied and is usually immediately replayed to break the tie.')
    pass


def Win_or_Lose(p_ch):  # Returns win ,tie or lose
    com_ch = choices[random.randint(0,2)]
    if p_ch == com_ch :
        return 1
    if com_ch=="rock":
        if p_ch=="paper":
            return 2
        elif p_ch == "scissors":
            return 0
    elif com_ch == "paper":
        if p_ch=="rock":
            return 0
        elif p_ch == "scissors":
            return 2
    elif com_ch == "scissors":
        if p_ch=="paper":
            return 0
        elif p_ch == "rock":
            return 2


def Play():
    u=User()
    play = True
    Menu()
    while play:
        choice = input("\nEnter your choice (Rock/Paper/Scissors) : ")
        if choice.lower() in choices:
            result = Win_or_Lose(choice)
            u.update_points(result)  # Here according to result we update points (+3,+1,-1)
            data = u.return_data()   # Appends the user's choice
            data.append(choice)
            if result == 2:
                print("\nMatch Won")
                data.append("Won")
            elif result ==1:
                print("\nTie Match")
                data.append("Tie")
            elif result == 0:
                print("\nMatch Lose")
                data.append("Lose")
            FileIO(data) 
        else:
            print("\nYou have given a wrong input as a choice")
            play = Redo()
            continue
        print(u)
        if not Redo() :
            play = False


def Menu():
    rules = input("\nDo you want to read the rules? (Y/N) : ")
    if rules == "Y" or rules == "y":
        Game_rules()


def Redo(): 
    c=input("\nDo you want to play again? (Y/N) :")
    if c == "Y" or c =="y":
        return True
    else:
        return False


def FileIO(l:list):  # To include the file inputs in a csv file for ML and record keeping
    
    filename = "Game_records.csv"
    with open(filename,"a+",newline='') as csv_file:
        filesize = os.path.getsize(filename)
        fields = ["Name","Score","User_choice","Result"]
        csv_w = csv.writer(csv_file)
        if filesize == 0:
        # Here create a new file and start
            csv_w.writerow(fields)
            csv_w.writerow(l)

        else:
        # Here insert new data
            csv_w.writerow(l)
             

    pass  # TODO: Make 2 files one with all records and another with 10 highest scores 
          # (Also after achieving high score ask to include and not if not selected)


if __name__=="__main__":
    print("\n----------------------------------------------------------------------------------------------------------")
    print("\nWelcome to the game of rock paper and scissors")
    Play()
    print("\n----------------------------------------------------------------------------------------------------------")
    pause("\n\nGame Finished!!! \n\nPress any key to exit....")