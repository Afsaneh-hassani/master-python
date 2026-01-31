# به دلیل شرایط فعلی اینترنت ایران و عدم امکان استفاده از گیتهاب کد مورد نظر را به این صورت ارسال کردم. امیدوارم تصحیح شود.


# imports and global variables



# getting user input

def get_user_input():
    user_word=input('please write your considered word: ')
    return user_word



# function of a palindrome string

def palindrome_string(user_input):
    word_length= len(user_input)
    
    if user_input[0] == user_input[word_length-1]:
        print('The string is a palindrome.')
    else:
        print('The string is not a palindrome.')
    

# check the user input
def main():
    user_word=get_user_input()
    palindrome_string(user_word)
    
    
# main function   
    
if __name__=="__main__":
    main()
    





