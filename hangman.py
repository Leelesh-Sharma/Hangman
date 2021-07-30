import random
from words import words
import string

def get_valid_word(words):
    
    word = random.choice(words)

    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    #print(word_letters) 

    alphabet = set(string.ascii_uppercase) 
    used_letters = set()

    while len(word_letters) > 0:
        
        print("You have already used this letter."," ".join(used_letters))
        
        # W - R D 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: "," ".join(word_list))

        user_letters = input("Type something: ").upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
        
        elif user_letters in used_letters:
            print("Try something else.You already used this letter.\n")
        
        else:
            print("Invalid character\n")
    
    print(f"\n{word}!!!")

hangman()
