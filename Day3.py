print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("WELCOME TO THE TREASURE ISLAND")

print("\n\n\n\n\n\n")
print("The Rules of the game are very simple.\n\nYou need to make the correct choice in order to WIN the game.")
choice1=input("You are standing between a crossroad.Make a choice to go 'left' or 'right'. \nHINT:The right side is not always right.")
CHOICE1=choice1.lower()
if CHOICE1=="left":
    print("Congratulations!! You made a wise choice.\n\nYou kept walking to the left and reached a river.\n\nYou again have twp choices.\n\nYou can cross the river with the help of a boat to cross it really fast or can walk through a broken bridge.\nMake a choice by choosing your way.")
    choice2=input("Write 'B' for a boat and 'b' for a bridge.")
    if choice2=='b':
        print("Hurrah! You cleared this round.\n\nWelcome to the last round of the game.\n\nThere are three doors in front of you.\nRED       GREEN       YELLOW\nMake a choice to win the game.\n")
        choice3=input("Type 'R' for Red, 'G' for green and 'Y' for Yellow.")
        CHOICE3=choice3.upper()
        if CHOICE3=='Y':
            print("Congratulations !!!! You are the Winner of the game.")
            print("Do you want your gift?")
            gift=input("Say 'Y' for yes and 'N' for no.")
            GIFT=gift.lower()
            if GIFT=='y':
                print('''
                 _________________
     |'-========OoO===='-.
     | ||'-.____'-.'-.____'-.
     | ||  |      |  |      |
      '-|  |      |  |      | Congooo! You became the winner!
         '-|______|__|______|
            '-.--./**).--.-'
                .' .'
               /__\
              //  \\
              `-   `-
              ''')
            else:
                print("You have successfully completed the game.THANK YOU.")
        else:
            print("GAME OVER.YOU MADE A WRONG CHOICE.")
    else:
        print("GAME OVER.YOU WERE EATEN BY A CROCODILE.")
        print('''
                            .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-

          ''')
else:
    print("GAME OVER. THERE WERE GHOSTS ON THE RIGHT SIDE OF THE CROOSROAD.")
    print('''
               ,
        .--')
       /    /
      |    /
   /`.\   (_.'\
   \          /
    '--. .---'
jgs   ( " )
       '-'
                ,
                 \`-,      ,     =-
             .-._/   \_____)\
            ("              / =-
             '-;   ,_____.-'       =-
  jgs         /__.'


       .-.
      ( " )
   /\_.' '._/\
   |         |
    \       /
     \    /`
   (__)  /
jgs`.__.'

''')
