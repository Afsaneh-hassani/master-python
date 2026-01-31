# constant variables list
import random
USER_CHOISES= ('rock','paper','scissors')

# input user choice
def get_user_input():
    user_choice= input('please pick your choice (rock, paper, scissors): ')
    while user_choice not in USER_CHOISES:
        user_choice= input('please pick your choice (rock, paper, scissors): ')
        
    return user_choice
        

 # input computer choice
 
def get_pc_input():
     
    pc_choice= random.choice(USER_CHOISES)
    print(f'user choice was {pc_choice}')
    return pc_choice
     
 
 # compare and determine the winner
 
def determine_winner(user_choice,pc_choice):
    if user_choice ==pc_choice:
        return 'CRAW!'
    elif (user_choice=='rock' and pc_choice=='scissors')\
        or (user_choice=='scissors' and pc_choice=='paper')\
        or (user_choice=='paper' and pc_choice=='rock'):
        print('user is winner')
    else:
        print('pc is winner')
     
# main function for whole of game


def main():
    user_input=get_user_input()
    pc_input=get_pc_input()
    determine_winner(user_input,pc_input)
    print('end of game')
    

 
 
 
 
 # quit game
answer= 'y'

while answer =='y':
    main()
    answer= input('do you want quir game? (y/n): ')