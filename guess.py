import string

### IMPORTANT: Fix this script later, it is kind of bad and the algorithm needs to be improved.

# Sub Functions

def guess_number():
    guesses = input("Enter the amount of guesses: ")

    if not guesses.isdigit():
        print("Invalid respnose.")
        return

    min_number = input("Enter the minimum number: ")

    if not min_number.isdigit():
        print("Invalid response.")
        return

    min_number = int(min_number)

    max_number = input("Enter the maximum number: ")

    if not max_number.isdigit():
        print("Invalid response.")
        return

    max_number = int(max_number)

    even_or_odd = input("Is the number even or odd: ")

    if even_or_odd.lower() not in ["even", "odd"]:
        print("Invalid response.")
        return

    if even_or_odd.lower() == "even":
        if min_number % 2 != 0:
            min_number += 1
        if max_number % 2 != 0:
            max_number -= 1
    elif even_or_odd.lower() == "odd":
        if min_number % 2 == 0:
            min_number += 1
        if max_number % 2 == 0:
            max_number -= 1

    close_to = input("Is the number closer to the beginning, middle, or end: ")

    if close_to.lower() not in ["beginning", "middle", "end"]:
        print("Invalid response.")
        return

    if close_to.lower() == "beginning":
        target_number = min_number
    elif close_to.lower() == "middle":
        target_number = (min_number + max_number) // 2
    elif close_to.lower() == "end":
        target_number = max_number

    while True:
        guess = target_number

        response = input(f"Is your number {guess}? (Enter 'higher', 'lower', or 'yes'): ")
        
        if response not in ["higher", "lower", "yes"]:
            print("Invalid response.")
            return

        if response == "higher":
            min_number = guess + 1
        elif response == "lower":
            max_number = guess - 1
        elif response == "yes":
            print("I guessed it! Your number is: ", guess)
            return

        if max_number < min_number:
            print("Sorry, I couldn't guess your number.")
            return

        target_number = (min_number + max_number) // 2

def guess_letter():
    alphabet = string.ascii_lowercase

    close_to = input("Is the letter closer to the beginning, middle, or end: ")

    if close_to.lower() not in ["beginning", "middle", "end"]:
        print("Invalid response.")
        return

    if close_to.lower() == "beginning":
        letter = alphabet[0]
    elif close_to.lower() == "middle":
        letter = alphabet[len(alphabet) // 2]
    elif close_to.lower() == "end":
        letter = alphabet[-1]

    response = input(f"Is your letter {letter}? (Enter 'higher', 'lower', or 'yes'): ")

    if response not in ["higher, lower, yes"]:
        print("Invalid response.")
        return

    while response != "yes":
        if response == "higher":
            index = alphabet.index(letter) + 1

            if index >= len(alphabet):
                print("Sorry, I couldn't guess your letter.")
                return

            letter = alphabet[index]
        elif response == "lower":
            index = alphabet.index(letter) - 1

            if index < 0:
                print("Sorry, I couldn't guess your letter.")
                return

            letter = alphabet[index]

        response = input(f"Is your letter {letter}? (Enter 'higher', 'lower', or 'yes'): ")

    print("I guessed it! Your letter is: ", letter)

def guess_symbol():
    symbols = "!@#$%^&*()"
    even_or_odd = input("Is the symbol even or odd: ")

    if even_or_odd.lower() not in ["even", "odd"]:
        print("Invalid response.")
        return

    if even_or_odd.lower() == "even":
        symbol = symbols[0::2][-1]
    else:
        symbol = symbols[1::2][-1]

    print("I am guessing that your symbol is: ", symbol)

# Main Functions

def main():
    print("Hello. Input a response (ex: exit).")
    print("Choices: [1] Number [2] Letter [3] Symbol [4] Exit")

    response = input("Reponse: ")

    if response.lower() in [4, "quit", "exit"]:
        quit()

    if not response.isdigit():
        print("Reponse must be a number.")
        return

    response = int(response)

    if response not in [1, 2, 3]:
        print("Invalid response.")
        return

    if response == 1:
        guess_number()
    elif response == 2:
        guess_letter()
    elif response == 3:
        guess_symbol()

if __name__ == "__main__":
    main()
