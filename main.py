import random
from sys import exit
from time import sleep
from os import system, name


def main():
    user_score = 0
    dictionary = read_from_file("dictionary.txt")
    clear_screen()

    # Shows the user a menu with choices.
    while True:
        menu_choice = input("\n[D]ictionary, [Q]uiz, [S]core, [E]xit: ")
        clear_screen()
        if menu_choice.upper() == "D":
            print_formatted_dictionary(dictionary)
        elif menu_choice.upper() == "Q":
            user_score += vocabulary_quiz(dictionary)
        elif menu_choice.upper() == "S":
            print(f"\nYour score: {user_score}")
        elif menu_choice.upper() == "E":
            user_quit(user_score)


def read_from_file(filename: str):
    # Returns the content of a file in the form of a dictionary.
    new_dictionary = {}
    try:
        f = open(filename, 'r')
        for line in f:
            # Assume keys and values are seperated with a colon.
            key = line.split(":")[0]
            value = line.split(":")[1]
            # Remove linebreaks.
            key = key.strip("\n")
            value = value.strip("\n")
            # Add the key and value to our dictionary.
            new_dictionary.update({key: value})
        f.close()
        return new_dictionary
    except OSError:
        print(f"\n Error: Could not find {filename}.\nMake sure it's located in the same directory as this program.\n")
        exit()
    except IndexError:
        print(f"\n Error: Could not read from {filename}. Make sure it doesn't contain empty lines.\n")
        exit()


def pick_a_random_key_or_value(input_dictionary: dict):
    # Returns a random value-key pair from a dictionary.
    # Since we can't pick random from a dict we put it's content in a list for this function to work.
    key, value = random.choice(list(input_dictionary.items()))
    # Randomly pick if we return the key or the value first.
    if random.randint(1, 2) == 1:
        return key, value
    else:
        return value, key


def print_formatted_dictionary(input_dictionary: dict):
    # Show the content of a dictionary with custom formatting.
    print("")
    for key, value in input_dictionary.items():
        if len(key) < 7:
            print(key, '\t\t\t', value)
        else:
            print(key, '\t\t', value)


def vocabulary_quiz(input_dictionary: dict):
    # Ask the user a question. User get a limited number of attempts.
    # Function returns 1 if the answer is correct and 0 if not.
    the_word, the_translation = pick_a_random_key_or_value(input_dictionary)

    max_number_of_tries = 3
    number_of_tries = 0
    while number_of_tries < max_number_of_tries:
        users_answer = input(f"Translate this:\n\t{the_word}\nTranslation:\n\t")
        if users_answer.lower() == the_translation.lower():
            print("Correct!\n")
            return 1
        else:
            number_of_tries += 1
            if number_of_tries == (max_number_of_tries - 1):
                print(f"Incorrect! You have 1 try left.\n")
            else:
                print(f"Incorrect! You have {max_number_of_tries - number_of_tries} tries left.\n")
    return 0


def user_quit(score: int):
    # Shows the users score before exiting.
    print(f"\nGoodbye! You achieved a total score of {score} points.\n")
    sleep(2)
    exit()


def clear_screen():
  # Clears the screen. nt = windows, if not we assume it's mac\linux.
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')


# Call main if not a module.
if __name__=="__main__": 
    main()
