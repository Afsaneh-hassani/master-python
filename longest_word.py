# import modules and global variables





# get user sentence

def user_input():
    user_input=input('please write your sentence: ')
    return user_input
    



# function of longest word in sentence
word_dict={}
def longest_word(user_input):
    user_input=user_input.split()
    for words in user_input:
        word_length=len(words)
        word_dict[words]=word_length
    largest_num=max(word_dict.values())
    
    print('Longest word(s):')
    for k , v in word_dict.items():
        if v==largest_num:
            print(f'{k} ({v} letters)')
    
        
    



# main function
def main():
    
    input_sentence=user_input()

    longest_word(input_sentence)
    
    


main()
    