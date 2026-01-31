# global variables
import random
MIN_NUM=1
MAX_NUM=10

# generate the random number
def generate_random_num():
    return random.randint(MIN_NUM,MAX_NUM)


# get guessed number of user
def get_user_input():
    print(f'your number should be between {MIN_NUM}-{MAX_NUM}')
    while True:
        try:
            user_input=int(input('please enter your guessed number: '))
        except ValueError:
            print('your number is nat valid')
        else:
            return user_input 



# comparison of user input and random number
def check_guessed_num(user_input,random_num):
    return user_input == random_num


# main function
def main():

    max_guessed_counts=3

    random_num=generate_random_num()
    print(random_num)

    while max_guessed_counts > 0:
        user_input=get_user_input()
        if check_guessed_num(user_input,random_num):
            print ('you have guessed right!!!')
        
            break
        max_guessed_counts-=1
        print(f'you can guesse {max_guessed_counts} times more') 
    else:
        print('you could not guess right number!! ')
        
    
    
    
if __name__=='__main__':
    main()
    
    
    
    