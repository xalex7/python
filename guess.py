import random
def main():
    def guessing_game():
        lowest = 1
        highest = 100
        attempts = 1 # since the user will be asked at least once, and then every time it loops will add 1 (similar to do-while in other languages);
        print("This program has you, the user, choose a number between 1 and 100.\nThen I, the computer, will try my best to guess it.\n\nIf I guess a number that’s SMALLER than the\nsecret number, respond by typing the letter s.\n\nIf I guess a number that’s BIGGER than the secret number,\nrespond by typing the letter b,\n\nand if I guess CORRECTLY,\nrespond by typing the letter c.\n")
        guess = random.randint(lowest, highest)
        answer = input(f"Is it {guess}? (type s,b,or c): ")
        while answer != 'c':
            attempts += 1
            if answer == 'b':
                lowest = guess + 1 # If the correct answer is bigger, the old guess should become the new lowest in range + 1;
                guess = random.randint(lowest, highest)
            elif answer =='s':
                highest = guess - 1 # If the correct answer is smaller, the old guess should become the new highest in range - 1;
                guess = random.randint(lowest, highest)
            answer = input(f"Is it {guess}? (type s,b,or c):")

        print(f"I got it after making just {attempts} guesses!")




    guessing_game()
main()