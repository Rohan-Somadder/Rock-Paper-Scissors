import random
from getch import pause

class user:
    def __init__(self):
        self.name=input("\nEnter your name : ")
        self.points = 0

    def update_points(self):
        self.points+=1
    
    def __str__(self):
        return "\nYour score is: "+ str(self.points)

choices = ['rock','paper','scissors']

def Game_rules():
    pass

def win_or_lose(p_ch):                  #returns win ,tie or lose
    com_ch = choices[random.randint(0,2)]
    if p_ch == com_ch :
        return 1
    if com_ch=='rock':
        if p_ch=='paper':
            return 2
        elif p_ch == 'scissors':
            return 0
    elif com_ch == 'paper':
        if p_ch=='rock':
            return 0
        elif p_ch == 'scissors':
            return 2
    elif com_ch == 'scissors':
        if p_ch=='paper':
            return 0
        elif p_ch == 'rock':
            return 2
    
def play():
    u=user()
    play = True
    menu()
    while play:
        choice = input("\nEnter your choice (Rock/Paper/Scissors) : ")
        if choice.lower() in choices:
            result = win_or_lose(choice)
            if result == 2:
                print('\nMatch Won')
                u.update_points() 
            elif result ==1:
                print('\nTie Match')
            elif result == 0:
                print('\nMatch Loose')
        else:
            print("\nYou have given a wrong input as a choice")
            play = redo()
            continue
        print(u)
        if not redo() :
            play = False

def menu():
    rules = input("\nDo you want to read the rules? (Y/N) : ")
    if rules == 'Y' or rules == 'y':
        Game_rules()

def redo():
    
    c=input("\nDo you want to play again? (Y/N) :")
    if c == 'Y' or c =='y':
        return True
    else:
        return False

if __name__=="__main__":
    print('Welcome to the game of rock paper and scissors')
    play()
    print('\n----------------------------------------------------------------------------------------------------------')
    pause("\n\nGame Finished!!! \n\nPress any key to exit....")