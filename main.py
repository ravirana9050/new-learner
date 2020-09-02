import random_word_generator
def change_word_state(selected_word, current_word_state, character):
    modified_word_state=""
    for i in range(len(selected_word)):
        if current_word_state[i]=='_' and character == selected_word[i]:
            modified_word_state += character
        else:
            modified_word_state += current_word_state[i]
    return modified_word_state

def input_character_in_word(selected_word,input_char,current_word_state,attempts_remaining):
    if input_char in selected_word:
        current_word_state=change_word_state(selected_word,current_word_state,input_char)
    else:
        attempts_remaining -= 1
    return current_word_state,attempts_remaining

def print_current_state(current_word_state,attempts_remaining):
    print("current state: ", end=" ")

    for i in current_word_state:
        print(i, end=" ")
    print("      atttempts remaining: ", attempts_remaining)

def check_game_status(selected_word,current_word_state,attempts_remaining):
    if current_word_state == selected_word:
        print("")
        print("winner winner chicken dinner!")
        print("")
        return True
    if attempts_remaining ==0:
        print("")
        print("better luck next time")
        return True
    return False

def play_game():
    attempts =5
    selected_word=random_word_generator.pic_random_word()

    current_word_state=""
    for i in range(len(selected_word)):
        if selected_word[i] in ['a','e','i','o','u']:
            current_word_state += selected_word[i]
        else:
            current_word_state += '_'
    attempts_remaining=attempts
    print_current_state(current_word_state,attempts_remaining)

    while True:
        input_char= input("guess a character: ")
        print("\n")

        current_word_state,attempts_remaining=input_character_in_word(selected_word,input_char,current_word_state,attempts_remaining)
        print_current_state(current_word_state,attempts_remaining)
        ended=check_game_status(selected_word,current_word_state,attempts_remaining)
        if ended:
            break

play_game()
