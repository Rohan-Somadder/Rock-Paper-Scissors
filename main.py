'''
Program to play rock paper scissors
made by - Rohan Somadder

# TODO: Make 2 files one with all records and another with 10 highest scores
    # (Also after achieving high score ask to include and not if not selected)
'''
import random
import os
import csv
from getch import pause

choices = ["rock", "paper", "scissors"]


class User:
    '''
    User class for storing the information about the current user\
    and updating them during in-game time
    '''

    def __init__(self):
        self.name = input("\nEnter your name : ")
        self.points = 0

    def update_points(self, result):
        '''
        Updates points of user according to the input type given (2:Win, 1:Tie, 0: Loose)
        '''
        if result == 2:
            self.points += 3
        elif result == 1:
            self.points += 1
        elif result == 0:
            self.points -= 1

    def return_data(self):
        '''
        Returns the name and points of user in form of list to inserted in records
        '''
        return [self.name, self.points]

    def __str__(self):
        return "\nYour score is: " + str(self.points)


def game_rules():
    '''
    Displays the basic rules for the game
    '''
    print('\nA player who decides to play rock will beat another player who has chosen scissors\
         ("rock crushes scissors"),\
         \nbut will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a\
         play of scissors ("scissors cuts paper").\
         \nIf both players choose the same shape, the game is tied and is usually immediately\
         replayed to break the tie.')


def win_or_loose(p_ch):
    '''
    Returns win, tie or lose according the situations
    '''
    com_ch = choices[random.randint(0, 2)]
    if p_ch == com_ch:
        return 1
    if com_ch == "rock":
        if p_ch == "paper":
            return 2
        elif p_ch == "scissors":
            return 0
    elif com_ch == "paper":
        if p_ch == "rock":
            return 0
        elif p_ch == "scissors":
            return 2
    elif com_ch == "scissors":
        if p_ch == "paper":
            return 0
        elif p_ch == "rock":
            return 2


def play():
    '''
    Main function for the game
    '''
    user = User()
    play_ = True
    rules = input("\nDo you want to read the rules? (Y/N) : ")
    if rules in ['Y', 'y']:
        game_rules()
    while play_:
        choice = input("\nEnter your choice (Rock/Paper/Scissors) : ")
        if choice.lower() in choices:
            result = win_or_loose(choice)
            # Here according to result we update points (+3,+1,-1)
            user.update_points(result)
            data = user.return_data()   # Appends the user's choice
            data.append(choice)
            if result == 2:
                print("\nMatch Won")
                data.append("Won")
            elif result == 1:
                print("\nTie Match")
                data.append("Tie")
            elif result == 0:
                print("\nMatch Lose")
                data.append("Lose")
            file_io(data)
        else:
            print("\nYou have given a wrong input as a choice")
            play_ = redo()
            continue
        print(user)
        if not redo():
            play_ = False


def redo():
    '''
    Asks wheather user wants to continue playing or to quit the game
    '''
    choice = input("\nDo you want to play again? (Y/N) :")
    if choice in ['Y', 'y']:
        return True
    return False


def file_io(lst: list):
    '''
    To include the file inputs in a csv file for ML and record keeping
    '''
    filename = "Game_records.csv"
    with open(filename, "a+", newline='', encoding='utf-8') as csv_file:
        filesize = os.path.getsize(filename)
        fields = ["Name", "Score", "User_choice", "Result"]
        csv_w = csv.writer(csv_file)
        if filesize == 0:
            # Here create a new file and start
            csv_w.writerow(fields)
            csv_w.writerow(lst)

        else:
            # Here insert new data
            csv_w.writerow(lst)


if __name__ == "__main__":
    print("\n------------------------------------------------\
        ----------------------------------------------------------")
    print("\nWelcome to the game of rock paper and scissors")
    play()
    print("\n------------------------------------------------\
        ----------------------------------------------------------")
    pause("\n\nGame Finished!!! \n\nPress any key to exit....")
