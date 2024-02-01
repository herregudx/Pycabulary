import random

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
    for key, value in input_dictionary.items():
        if len(key) < 7:
            print(key, '\t\t\t', value)
        else:
            print(key, '\t\t', value)


def vocabulary_quiz():
    the_word, the_translation = pick_a_random_key_or_value(dictionary)
    answer = input(f"Translate this:\n\t{the_word}\nTranslation:\n\t")
    if answer.lower() == the_translation.lower():
        print("Yay!")
    else:
        print("Try again!")


dictionary = read_from_file("dictionary.txt")
print_formatted_dictionary(dictionary)
vocabulary_quiz()



