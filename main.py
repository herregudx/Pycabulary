import random
from sys import exit
from time import sleep
from os import system, name


def main():
    user_score = 0
    dictionary = read_from_file("dictionary.txt")
    clear_screen()

    while True:
        menu_choices = input("\n[D]ictionary, [Q]uiz, [S]core, [E]xit: ")
        clear_screen()
        if menu_choices.upper() == "D":
            print_formatted_dictionary(dictionary)
        elif menu_choices.upper() == "Q":
            user_score += vocabulary_quiz(dictionary)
        elif menu_choices.upper() == "S":
            print(f"\nYour score: {user_score}")
        elif menu_choices.upper() == "E":
            user_quit(user_score)


def read_from_file(filename: str):
    new_dictionary = {}
    try:
        f = open(filename, 'r')
        for line in f:
            # Assume words are split with a colon
            word1 = line.split(":")[0]
            word2 = line.split(":")[1]
            # Remove linebreaks
            word1 = word1.strip("\n")
            word2 = word2.strip("\n")
            # Add the words to our dictionary
            new_dictionary.update({word1: word2})
        f.close()
        return new_dictionary
    except OSError:
        print(f"\n Error: Could not find {filename}.\nMake sure it's located in the same directory as this program.\n")
        exit()
    except IndexError:
        print(f"\n Error: Could not read from {filename}. Make sure it doesn't contain empty lines.\n")
        exit()


def pick_a_random_key_or_value(input_dictionary: dict):
    # Since we can't pick random from a dict we put it's content in a list for this function to work
    key, value = random.choice(list(input_dictionary.items()))
    # Randomly pick if we return the key or the value first
    if random.randint(1, 2) == 1:
        return key, value
    else:
        return value, key


def print_formatted_dictionary(input_dictionary: dict):
    print("")
    for key, value in input_dictionary.items():
        if len(key) < 7:
            print(key, '\t\t\t', value)
        else:
            print(key, '\t\t', value)


def vocabulary_quiz(input_dictionary: dict):
    the_word, the_translation = pick_a_random_key_or_value(input_dictionary)
    
    # User get a limited amount of attempts.
    max_number_of_tries = 3
    number_of_tries = 0
    while True and number_of_tries < max_number_of_tries:
        answer = input(f"Translate this:\n\t{the_word}\nTranslation:\n\t")
        if answer.lower() != the_translation.lower():
            number_of_tries += 1
            if number_of_tries == (max_number_of_tries - 1):
                print(f"Incorrect! You have 1 try left.\n")
            else:
                print(f"Incorrect! You have {max_number_of_tries - number_of_tries} tries left.\n")
        elif answer.lower() == the_translation.lower():
            print("Correct!")
            return 1
    return 0


def user_quit(score: int):
    print(f"\nGoodbye! You achieved a total score of {score} points.\n")
    sleep(2)
    exit()


def clear_screen():
  # Clears the screen. nt = windows, if not we assume it's mac\linux
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')


# call main if not a module
if __name__=="__main__": 
    main() 